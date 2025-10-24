import json
import os

class Settings:
    _settings = {}
    _FILE_PATH = None
    _FILE_NAME = "settings.json"
    REQUIRED_KEYS = ["random", "lang", "save_at", "use_regex", "recursive_search", "directory", "margin_in_milliseconds"]

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
            try:
                with open(cls._FILE_PATH, 'r') as f:
                    cls._settings = json.load(f)
                    if cls.__verify_settings(cls._settings) is not True:
                        cls.reset_to_default()
            except Exception as e:
                print(e)
                cls.reset_to_default()

    @classmethod
    def __verify_settings(cls, settings: dict) -> bool:
        return set(settings.keys).issubset(set(cls.REQUIRED_KEYS))

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
            "use_regex": False,
            "recursive_search": True,
            "directory": None, # Where to search
            "margin_in_milliseconds": 2000
        }
        cls.__rewrite_to_file()

    @classmethod
    def get_settings(cls) -> dict: cls._settings

    @classmethod
    def set_settings(cls, settings: dict):
        if cls.__verify_settings(settings) is not True:
            raise ValueError()
        for key, value in settings:
            cls._settings[key] = value
        cls.__rewrite_to_file()

Settings.__class_initialize()