from converter import Converter
from csvtypes import CSVRow
from typing import List
from potypes import po_format_mapping, POField
import csv
import os


class ConverterCSV2Po(Converter):

    @staticmethod
    def convert(path: str):
        if os.path.isdir(path):
            files = [f for f in os.listdir(path) if f.endswith('.csv')]

            converted = False
            for file in files:
                converted |= ConverterCSV2Po.convert_file(file)

            return converted
        elif os.path.isfile(path) and path.endswith('.csv'):
            return ConverterCSV2Po.convert_file(path)
        else:
            return False

    @staticmethod
    def convert_file(filepath: str):
        rows: List[CSVRow] = []
        file_string = ""
        with open(filepath, newline='', encoding='utf-8') as f:
            next(f)

            reader = csv.reader(f)

            for row in reader:
                print(row)

                csv_row = CSVRow()
                csv_row.parse_from_array(row)

                po_field: POField = ConverterCSV2Po.convert_row_to_po_field(csv_row)

                file_string += str(po_field) + '\n\n'

        with open(f'{filepath}.po', 'w', encoding='utf-8') as the_file:
            the_file.write(file_string)

        print(f'{filepath} converted')

        return True


    @staticmethod
    def convert_row_to_po_field(row: CSVRow) -> POField:
        po_field = POField()

        for var, val in vars(row).items():
            vars(po_field)[var] = vars(row)[var]

        print(po_field)

        return po_field
