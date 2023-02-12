from converter import Converter
from csvtypes import CSVRow
from typing import List
from potypes import po_format_mapping


class ConverterPo2CSV(Converter):

    @staticmethod
    def convert(filepath: str):

        rows: List[CSVRow] = []
        row: CSVRow = None

        for line in open(filepath, encoding='utf-8'):
            if line == "\n":
                if row is not None:
                    row.fill_empty()
                    print(row)
                    rows.append(row)
                    row = CSVRow()
                else:
                    row = CSVRow()
            else:
                if row is None:
                    continue

                line_parts = line.split(" ")
                context: str = line_parts[0]
                record: str = line.removeprefix(f'{context} ')  # note the whitespace after context
                record = record.rstrip()

                for key, value in po_format_mapping.items():
                    if context == value:
                        vars(row)[key] = vars(row)[key].format(record=record)

        csv_content = CSVRow.get_header_row()
        csv_content += '\n'

        for row in rows:
            csv_content += str(row)
            csv_content += '\n'

        with open(f'{filepath}.csv', 'a') as the_file:
            the_file.write(csv_content)

        return True
