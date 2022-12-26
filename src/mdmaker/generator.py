from mdmaker import MdMaker


class Generator:
    def __init__(self, filename: str, mode: str) -> None:
        self.mdmaker = MdMaker()
        self.filename = filename
        self.mode = mode
        self.content = ''

    def save_file(self):
        with open(self.filename, self.mode) as f:
            f.write(self.content)

    def add_header(self, level: int, text: str):
        header = self.mdmaker.header(level=level, text=text)
        self.content += '{}{}\n'.format('\n' if self.content else '', header)

    def add_paragraph(self, text: str, is_bold: bool = False,
                      is_italic: bool = False, indents: int = 0):
        paragraph = self.mdmaker.paragraph(text, is_bold, is_italic, indents)
        self.content += '{}{}\n'.format(
            '\n' if self.content else '', paragraph)

    def add_text(self, text: str, is_bold: bool = False,
                 is_italic: bool = False, spaces: int = 1):
        self.content += self.mdmaker.text(text, is_bold, is_italic, spaces)

    def add_line(self, text: str, is_bold: bool = False,
                 is_italic: bool = False, indents: int = 0):
        line = self.mdmaker.line(text, is_bold, is_italic, indents)
        self.content += '{}\n'.format(line)
