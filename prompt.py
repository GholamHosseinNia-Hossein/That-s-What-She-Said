import argparse

class Prompt:
    
    def __init__(self):
        self._args = self.__init_args()
        pass

    # Private
    # --------------------------------

    def __init_args(self) -> argparse.ArgumentParser:
        # Initializes the argument parser
        # Sets the description and usage of the program
        parser = argparse.ArgumentParser(description="Prompt for the user")
        parser.add_argument("-s", "--start", action="store_true", type= bool, help="Start the clipping procedure")
        parser.add_argument("-e", "--end", action="store_true", type= bool, help="End the program")
        parser.add_argument("--use_regex", action="store_true", type= bool, help="Shall we use 'regex' to search for the desired phrase?")
        parser.add_argument("--random", type=bool, action="store_true", help="Shall I select a random phrase instance?")
        parser.add_argument("--directory", help="Where I searech for subtitles")
        parser.add_argument("--recursive_search", type=bool, action="store_true", help="Do I search your directory recursively?")
        parser.add_argument("--save_at", help="Only the saving directory. Do not include file name!")
        parser.add_argument("--file_name", help="Only the saved file's name. Do not include directory")
        parser.add_argument("--lang", choices=["en", "fa", "fr"], help= "Choose a language: en, fr, fa")
        parser.add_argument("--phrase", help="What to look for")
        parser.add_argument("--margin_in_milliseconds", type=int, help="How much to cut out of the video, before and after")

        return parser

    # Public
    # --------------------------------

    def parse_args(self):
        return self._args.parse_args()
    
    def print_help(self) -> None:
        self._args.print_help()

    def get_args(self) -> dict:
        return {"use_regex": self._args.use_regex,
                "lang": self._args.lang,
                "directory": self._args.directory,
                "recursive_search": self._args.recursive_search,
                "phrase": self._args.phrase,
                "start": self._args.start,
                "end": self._args.end,
                "save_at": self._args.save_at,
                "file_name": self._args.file_name,
                "random": self._args.random,
                "margin_in_milliseconds": self._args.margin_in_milliseconds}

    ## Getters
    ## --------------------------------

    @property
    def save_at(self) -> str: self._args.save_at
    
    @property
    def directory(self) -> str: self._args.directory

    @property
    def recursive_search(self) -> bool: self._args.recursive_search

    @property
    def use_regex(self) -> bool: self._args.use_regex

    @property
    def start(self) -> bool: self._args.start

    @property
    def end(self) -> bool: self._args.end

    @property
    def lang(self) -> str: self._args.lang

    @property
    def phrase(self) -> str: self._args.phrase

    @property
    def file_name(self) -> str: self._args.file_name

    @property
    def select_random(self) -> bool: self._args.random

    @property
    def margin_in_milliseconds(self) -> int: self._args.margin_in_milliseconds