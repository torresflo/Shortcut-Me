import os

from Shortcuts import ShortcutList
from FileManager import FileManager

if __name__ == '__main__':
    shortcutList = ShortcutList()
    randomShortcut = shortcutList.getRandomShortcut()

    fileName = os.getenv("MARKDOWN_FILE")
    if fileName is not None:
        FileManager.writeRandomShortcutInFile(fileName, randomShortcut)
    else:
        raise Exception(f"Cannot find environment variable: MARKDOWN_FILE")
