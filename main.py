from Shortcuts import ShortcutList
from FileManager import FileManager

if __name__ == '__main__':
    shortcutList = ShortcutList()
    randomShortcut = shortcutList.getRandomShortcut()

    FileManager.writeRandomShortcutInFile(FileManager.DefaultReadmeFileName, randomShortcut)
