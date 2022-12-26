from .helpers import add_words


class MdMaker:
    def header(self, level: int, text: str) -> str:
        return f'{"#" * level} {text.strip()}'

    def paragraph(self, text: str, is_bold: bool = False,
                  is_italic: bool = False, indents: int = 0):
        return add_words(text, True, False, is_bold, is_italic, indents)

    def text(self, text: str, is_bold: bool = False,
             is_italic: bool = False, spaces: int = 1):
        return add_words(text, False, False, is_bold, is_italic, spaces)

    def line(self, text: str, is_bold: bool = False,
             is_italic: bool = False, indents: int = 0):
        return add_words(text, False, True, is_bold, is_italic, indents)
