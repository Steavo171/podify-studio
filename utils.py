def read_text_from_file(file_path: str):

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
