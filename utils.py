from type import DialogListType


def readTextFromFile(file_path: str):

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def dialogListFromText(string: str,splitBy:str=";") -> DialogListType:

    dialogs = string.replace("\n", "").strip().split(splitBy)
    dialogs = [dialog.strip() for dialog in dialogs]

    dialogsList: DialogListType = []

    if dialogs[-1] == '':
        dialogs.pop()

    for i,text in enumerate(dialogs):
        name, text = text.split(":")
        dialogsList.append({"name": name, "text": text})

    return dialogsList




    



