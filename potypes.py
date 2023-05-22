po_format_mapping = {
    'comment': '#',
    'extra_comment': '#.',
    'format': '#,',
    'reference': '#:',
    'previous': '#|',
    'msgctxt': 'msgctxt',
    'msgid': 'msgid',
    'msgstr': 'msgstr'
}


class POField:
    def __init__(self):
        self.comment: str = '#',
        self.extra_comment: str = '#.',
        self.format: str = '#,',
        self.reference: str = '#:',
        self.previous: str = '#|',
        self.msgctxt: str = 'msgctxt',
        self.msgid: str = 'msgid',
        self.msgstr: str = 'msgstr'

    def __str__(self):
        return f'''# {self.comment}
#. {self.extra_comment}
#, {self.format}
#: {self.reference}
#| {self.previous}
msgctxt "{self.msgctxt}"
msgid "{self.msgid}"
msgstr "{self.msgstr}"'''

