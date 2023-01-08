import os

from Shortcuts import Shortcut

class FileManager:
    ShortcutBoxStartString = "<!-- shortcut-box start -->"
    ShortcutBoxEndString = "<!-- shortcut-box end -->"
    DefaultReadmeFileName = "README.md"

    def writeRandomShortcutInFile(fileName: str, shortcut: Shortcut):
        if os.path.exists(fileName):
            contentToWrite = FileManager.computeFileContentWithShortcut(fileName, shortcut)
            with open(fileName, "w", encoding="utf-8") as file:
                file.write(contentToWrite)

    def computeFileContentWithShortcut(fileName: str, shortcut: Shortcut) -> str:
        with open(fileName, "r", encoding="utf-8") as file:
            content = file.read()

            startLineNumber = content.find(FileManager.ShortcutBoxStartString)
            endLineNumber = content.find(FileManager.ShortcutBoxEndString)

            before = content[0:startLineNumber]
            after = content[endLineNumber:len(content)]
            
            newContent = before
            newContent += FileManager.computeShortcutString(shortcut)
            newContent += after
            return newContent

    def computeShortcutString(shortcut : Shortcut) -> str:
        string = f"{FileManager.ShortcutBoxStartString}\n"
        string += f"In {shortcut.m_editor}\n\n"
        for indexKeyGroup, keyGroup in enumerate(shortcut.m_shortcutKeys):
            for indexKey, key in enumerate(keyGroup):
                string += f"<kbd>{key}</kbd>"
                if indexKey < len(keyGroup) - 1:
                    string += " + "
            if indexKeyGroup < len(shortcut.m_shortcutKeys) - 1:
                string += ", "
        string += f" to `{shortcut.m_shortcutName}`\n"
        string += "<!-- Powered by https://github.com/torresflo/Shortcut-Me. -->\n"
        return string

                


    