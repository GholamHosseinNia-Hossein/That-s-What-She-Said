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
    def _class_initialize(cls):
        cls._FILE_PATH = os.path.join(os.getcwd(), cls._FILE_NAME)
        if not os.path.exists(cls._FILE_PATH):
            with open(cls._FILE_PATH, "w") as f:
                pass
        cls.__load_settings()

    @classmethod
    def __load_settings(cls):
            try:
                with open(cls._FILE_PATH, 'r') as f:
                    data = json.load(f)
                    if cls.__is_subset(data) is not True:
                        cls.reset_to_default()
                    else:
                        cls._settings = data
            except Exception as e:
                print(e)
                cls.reset_to_default()

    @classmethod
    def __is_subset(cls, settings: dict) -> bool:
        return set(settings.keys()).issubset(set(cls.REQUIRED_KEYS))

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
            "save_at": os.path.join(os.environ["USERPROFILE"], "Desktop"),
            "use_regex": False,
            "recursive_search": True,
            "directory": None, # Where to search
            "margin_in_milliseconds": 2000
        }
        cls.__rewrite_to_file()

    @classmethod
    def get_settings(cls) -> dict: return cls._settings

    @classmethod
    def set_settings(cls, settings: dict):
        filtered_setttings = cls.__filter_usable_rows(settings)
        if cls.__is_subset(filtered_setttings) is not True:
            raise ValueError()
        for key, value in filtered_setttings.items():
            cls._settings[key] = value
        cls.__rewrite_to_file()

    @classmethod
    def __filter_usable_rows(cls, rows: dict):
        filtered_rows: dict = {}
        for key, value in rows.items():
            if key in cls.REQUIRED_KEYS:
                filtered_rows[key] = value
        return filtered_rows

Settings._class_initialize()