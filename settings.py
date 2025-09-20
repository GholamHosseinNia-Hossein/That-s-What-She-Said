import json
import os

class Settings:
    _settings = {}
    _file_path = None

    def __init__(self):
        raise RuntimeError("'Settings' shall not be instantiated")

    # Methods
    # -------------------------------
    @classmethod
    def class_initialize(cls):
        cls.__load_settings()

    @classmethod
    def __load_settings(cls):
        if file_exists() and file_is_healthy():
            cls._settings = json.load(cls._file_path)
        else:
            cls.reset_to_default()

    @classmethod
    def __rewrite_to_file(cls):
        pass

    @classmethod
    def reset_to_default(cls):
        pass

Settings.__class_initialize()