import argparse

class Prompt:
    
    def __init__(self):
        self.__args = self.__init_args()
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
        parser.add_argument("--directory", help="Where I searech for subtitles")
        parser.add_argument("--save_at", help="Only the saving directory. Do not include file name!")
        parser.add_argument("--file_name", help="Only the saved file's name. Do not include directory")
        parser.add_argument("--lang", choices=["en", "fa", "fr"], help= "Choose a language: en, fr, fa")
        parser.add_argument("--phrase", help="What to look for")

        return parser

    # Public
    # --------------------------------

    def parse_args(self):
        return self.__args.parse_args()
    
    def print_help(self) -> None:
        self.__args.print_help()

    def get_args(self) -> dict:
        return {"use_regex": self.__args.use_regex,
                "lang": self.__args.lang,
                "directory": self.__args.directory,
                "phrase": self.__args.phrase,
                "start": self.__args.start,
                "end": self.__args.end,
                "save_at": self.__args.save_at,
                "file_name": self.__args.file_name}

    ## Getters
    ## --------------------------------

    @property
    def save_at(self) -> str: self.__args.save_at
    
    @property
    def directory(self) -> str: self.__args.directory

    @property
    def use_regex(self) -> bool: self.__args.use_regex

    @property
    def start(self) -> bool: self.__args.start

    @property
    def end(self) -> bool: self.__args.end

    @property
    def lang(self) -> str: self.__args.lang

    @property
    def phrase(self) -> str: self.__args.phrase

    @property
    def file_name(self) -> str: self.__args.file_name