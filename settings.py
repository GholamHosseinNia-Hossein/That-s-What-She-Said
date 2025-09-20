import json
import os

class Settings:
    _settings = {}
    _FILE_PATH = None
    _FILE_NAME = "settings.json"

    def __init__(self):
        raise RuntimeError("'Settings' shall not be instantiated")

    # Methods
    # -------------------------------

    @classmethod
    def __class_initialize(cls):
        cls._FILE_PATH = os.path.join(os.getcwd(), cls._FILE_NAME)
        cls.__load_settings()

    @classmethod
    def __load_settings(cls):
        if os.path.exists(cls._FILE_PATH):
            try:
                with open(cls._FILE_PATH, 'r') as f:
                    cls._settings = json.load(f)
            except Exception as e:
                print(e)
        else:
            cls.reset_to_default()

    @classmethod
    def __rewrite_to_file(cls):
        with open(cls._FILE_PATH, "w") as f:
            try:
                json.dump(cls._settings, f, indent=4)
            except Exception as e:
                print(e)

    @classmethod
    def reset_to_default(cls):
        cls._settings = {
            "random": True,
            "lang": "en",
            "save_as": os.path.join(os.environ["USERPROFILE"], "Desktop"),
            "regex": False
        }
        cls.__rewrite_to_file()

Settings.__class_initialize()