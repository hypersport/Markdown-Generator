class MdGenerator:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.content = ''

    def save_file(self):
        with open(self.filename, self.mode) as f:
            f.write(self.content)

    def add_header(self, level: int, text: str):
        pass

    def add_text(self, text: str):
        pass

    def add_bold_text(self, text: str):
        pass

    def add_italic_text(self, text: str):
        pass

    def add_bold_italic_text(self, text: str):
        pass
