from type import DialogListType


def readTextFromFile(file_path: str):
    """
    Read text from a file.

    Args:
        file_path: 
            The path to the file to read (str).

    Returns:
        The content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def dialogListFromText(string: str, splitBy: str = ";") -> DialogListType:
    """
    Convert a string containing dialog information into a list of dictionaries.

    Args:
        string: 
            The input string containing dialog information (str).

        splitBy:
            The delimiter used to separate dialogs (str).

    Returns:
        A list of dictionaries containing dialog information (DialogListType).
    """
    # Split the string into individual dialogs
    dialogs = string.replace("\n", "").strip().split(splitBy)
    dialogs = [dialog.strip() for dialog in dialogs]

    dialogsList: DialogListType = []

    # Remove the last empty element if present
    if dialogs[-1] == '':
        dialogs.pop()

    # Parse each dialog and append it to the dialogsList
    for dialog in dialogs:
        name, text = dialog.split(":")
        dialogsList.append({"name": name, "text": text})

    return dialogsList
