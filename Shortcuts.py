import os
import json
import random

class Shortcut(object):
    def __init__(self, editor: str, category: str, shortcut):
        self.m_editor = editor
        self.m_category = category
        self.m_shortcutName = shortcut["name"]
        self.m_shortcutKeys = shortcut["keys"]

    def __repr__(self) -> str:
        return f"<Shortcut for {self.m_editor} ({self.m_category}). {self.m_shortcutName} = {self.m_shortcutKeys}>"

class ShortcutList(object):
    DefaultDataFolder = "./data"
    DefaultDataFileName = f"{DefaultDataFolder}/shortcuts.json"
    
    def __init__(self):
        self.loadDataFromFile(ShortcutList.DefaultDataFileName)

    def loadDataFromFile(self, fileName: str):
        if os.path.exists(fileName):
            with open(fileName, "r", encoding="utf-8") as file:
                self.m_data = json.load(file)

    def getRandomShortcut(self):
        if self.m_data is not None:
            randomEditor = random.choice(self.m_data["editors"])
            randomCategory = random.choice(randomEditor["categories"])
            randomShortcut = random.choice(randomCategory["shortcuts"])

            return Shortcut(randomEditor["name"], randomCategory["name"], randomShortcut)