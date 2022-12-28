from .helpers import add_words


class MdMaker:
    def header(self, level: int, header: str) -> str:
        return '{} {}'.format('#' * level, header.strip())

    def paragraph(self, paragraph: str, is_bold: bool = False,
                  is_italic: bool = False, indents: int = 0) -> str:
        return add_words(paragraph, True, False, is_bold, is_italic, indents)

    def text(self, text: str, is_bold: bool = False,
             is_italic: bool = False, spaces: int = 1) -> str:
        return add_words(text, False, False, is_bold, is_italic, spaces)

    def line(self, line: str, is_bold: bool = False,
             is_italic: bool = False, indents: int = 0) -> str:
        return add_words(line, False, True, is_bold, is_italic, indents)

    def multi_paragraphs(self, paragraphs: list, is_bold: bool = False,
                         is_italic: bool = False, indents: int = 0) -> str:
        content = ''
        for paragraph in paragraphs:
            content += '\n'
            content += self.paragraph(paragraph, is_bold, is_italic, indents)
            content += '\n'
        return content.strip('\n')

    def multi_lines(self, lines: list, is_bold: bool = False,
                    is_italic: bool = False, indents: int = 0) -> str:
        content = ''
        for line in lines:
            content += self.line(line, is_bold, is_italic, indents)
            content += '\n'
        return content.strip('\n')

    def blockquote(self, quote: str) -> str:
        return '> {}'.format(quote.strip())

    def multi_blockquotes(self, quotes: list, is_splitted: bool = False) -> str:
        content = ''
        separator = '\n\n' if is_splitted else '\n>\n'
        sep_len = len(separator)
        for quote in quotes:
            content += self.blockquote(quote)
            content += separator
        return content[: -sep_len]
