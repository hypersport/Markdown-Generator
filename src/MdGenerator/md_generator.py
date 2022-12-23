class MdGenerator:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.content = ''

    def save_file(self):
        with open(self.filename, self.mode) as f:
            f.write(self.content)

    def add_header(self, level: int, text: str):
        self.content += f'{"\n" if self.content else ""}{"#" * level} {text.strip()}\n'

    def add_text(self, text: str, is_paragraph: bool = False, is_bold: bool = False,
                 is_italic: bool = False, spaces: int = 1):
        star_num = 0
        star_num = star_num + 1 if is_italic else star_num
        star_num = star_num + 2 if is_bold else star_num
        stars = '*' * star_num
        if is_paragraph:
            self.content += f'{"\n" if self.content else ""}{stars}{text.strip()}{stars}\n'
        else:
            self.content += f'{" " * spaces}{stars}{text.strip()}{stars}'
