import re


class CSVRow:
    def __init__(self):
        self.comment: str = ''
        self.extra_comment: str = ''
        self.format: str = ''
        self.reference: str = ''
        self.previous: str = ''
        self.msgctxt: str = ''
        self.msgid: str = ''
        self.msgstr: str = ''

    def fill_empty(self):
        for var, val in vars(self).items():
            if vars(self)[var] == '{record}' or vars(self)[var] == '"{record}"':
                vars(self)[var] = ''

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

    def get_as_array(self):
        return [
            self.msgid, 
            self.msgstr, 
            self.msgctxt, 
            self.comment, 
            self.extra_comment, 
            self.format, 
            self.reference, 
            self.previous
        ]
        
    def get_as_dict(self):
        return {
            'Orig': self.msgid, 
            'Text': self.msgstr, 
            'Tech': self.msgctxt, 
            'Comment': self.comment, 
            'Extra Comment': self.extra_comment, 
            'Format': self.format, 
            'Reference': self.reference, 
            'PrevVersion': self.previous
        }

    @staticmethod
    def get_header_row():
        return f'Orig,Text,Tech,Comment,Extra Comment,Format,Reference,PrevVersion'
        
    @staticmethod
    def get_headers():
        return ['Orig','Text','Tech','Comment','Extra Comment','Format','Reference','PrevVersion']
