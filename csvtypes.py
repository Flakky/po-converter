import re


class CSVRow:
    def __init__(self):
        self.comment: str = '"{record}"'
        self.extra_comment: str = '"{record}"'
        self.format: str = '"{record}"'
        self.reference: str = '"{record}"'
        self.previous: str = '"{record}"'
        self.msgctxt: str = '{record}'
        self.msgid: str = '{record}'
        self.msgstr: str = '{record}'

    def fill_empty(self):
        for var, val in vars(self).items():
            if vars(self)[var] == '{record}' or vars(self)[var] == '"{record}"':
                vars(self)[var] = '""'

    def __str__(self):
        return f'{self.msgid},{self.msgstr},{self.msgctxt},{self.comment},{self.extra_comment},{self.format},{self.reference},{self.previous}'

    def parse(self, string_row: str):
        print(f"Parsing CSV row {string_row}")

        # Thank you, ChatGPT for this. I do not know regex
        pattern = r'"((?:[^"]|"")*)"|([^,]+)'

        values = []
        fields = re.findall(pattern, string_row)

        for x in fields:
            if x[0] != '':
                values.append(x[0])
            values.append(x[1])

        self.parse_from_array(values)

    def parse_from_array(self, values):
        self.msgid = values[0]
        self.msgstr = values[1]
        self.msgctxt = values[2]
        self.comment = values[3]
        self.extra_comment = values[4]
        self.format = values[5]
        self.reference = values[6]
        self.previous = values[7]


    @staticmethod
    def get_header_row():
        return f'Orig,Text,Tech,Comment,Extra Comment,Format,Reference,PrevVersion'
