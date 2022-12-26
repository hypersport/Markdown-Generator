def add_words(text: str, is_paragraph: bool, is_line: bool,
              is_bold: bool, is_italic: bool, spaces: int) -> str:
    star_num = 0
    star_num = star_num + 1 if is_italic else star_num
    star_num = star_num + 2 if is_bold else star_num
    stars = '*' * star_num
    if is_paragraph:
        return '{0}{1}{2}{1}'.format('&nbsp;' * spaces, stars, text.strip())
    elif is_line:
        return '{0}{1}{2}{1}  '.format('&nbsp;' * spaces, stars, text.strip())
    else:
        return '{0}{1}{2}{1}'.format(' ' * spaces, stars, text.strip())
