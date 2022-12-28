from mdmaker import MdMaker


class Generator:
    def __init__(self, filename: str) -> None:
        self.mdmaker = MdMaker()
        self.filename = filename
        self.content = ''

    def save_file(self) -> None:
        with open(self.filename, 'w') as f:
            f.write(self.content)

    def add_header(self, level: int, header: str) -> None:
        header = self.mdmaker.header(level, header)
        self.content += '{}{}\n'.format('\n' if self.content else '', header)

    def add_paragraph(self, paragraph: str, is_bold: bool = False,
                      is_italic: bool = False, indents: int = 0) -> None:
        paragraph = self.mdmaker.paragraph(
            paragraph, is_bold, is_italic, indents)
        self.content += '{}{}\n'.format(
            '\n' if self.content else '', paragraph)

    def add_text(self, text: str, is_bold: bool = False,
                 is_italic: bool = False, spaces: int = 1) -> None:
        self.content += self.mdmaker.text(text, is_bold, is_italic, spaces)

    def add_line(self, line: str, is_bold: bool = False,
                 is_italic: bool = False, indents: int = 0) -> None:
        line = self.mdmaker.line(line, is_bold, is_italic, indents)
        is_first_line = len(self.content) > 0 and self.content[-3:] != '  \n'
        self.content += '{}{}\n'.format('\n' if is_first_line else '', line)

    def add_multi_paragraphs(self, paragraphs: list, is_bold: bool = False,
                             is_italic: bool = False, indents: int = 0) -> None:
        for paragraph in paragraphs:
            self.add_paragraph(paragraph, is_bold, is_italic, indents)

    def add_multi_lines(self, lines: list, is_bold: bool = False,
                        is_italic: bool = False, indents: int = 0):
        for line in lines:
            self.add_line(line, is_bold, is_italic, indents)

    def add_blockquote(self, quote: str) -> None:
        blockquote = self.mdmaker.blockquote(quote)
        self.content += '{}{}\n'.format(
            '\n' if self.content else '', blockquote)

    def add_multi_blockquotes(self, quotes: list, is_splitted: bool = False) -> None:
        blockquotes = self.mdmaker.multi_blockquotes(quotes, is_splitted)
        self.content += '{}{}\n'.format(
            '\n' if self.content else '', blockquotes)

    def add_lists(self, lists: dict) -> None:
        list_content = self.mdmaker.lists(lists)
        self.content += '{}{}\n'.format(
            '\n' if self.content else '', list_content)

    def add_lists_in_blockquotes(self, lists: dict, is_splitted: bool = False) -> None:
        block_content = self.mdmaker.lists_in_blockquotes(lists, is_splitted)
        self.content += '{}{}\n'.format(
            '\n' if self.content else '', block_content)
