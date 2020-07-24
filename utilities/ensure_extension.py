import os


def ensure_extension(file, extension):
    """
    Ensures the file in the :param file: has the extension :param extension:.  If it does not, append the extension.
    :return: Fixed file
    """
    root, ext = os.path.splitext(file)
    root, ext = root.lower(), ext.lower()
    if isinstance(extension, str):
        extension = f".{extension}".lower() if extension[0] != '.' else extension.lower()
    if ext == extension:
        return file
    return root + extension
