import argparse

class Prompt:
    
    def __init__(self):
        self.__parser = self.__init_args()
        self.__args = None

    # Private
    # --------------------------------

    def __init_args(self) -> argparse.ArgumentParser:
        # Initializes the argument parser
        # Sets the description and usage of the program
        parser = argparse.ArgumentParser(description="Prompt for the user")
        parser.add_argument("-s", "--start", action="store_true", help="Start the clipping procedure")
        parser.add_argument("-e", "--end", action="store_true", help="End the program")
        parser.add_argument("--use_regex", action="store_true", help="Shall we use 'regex' to search for the desired phrase?")
        parser.add_argument("--random", action="store_true", help="Shall I select a random phrase instance?")
        parser.add_argument("--directory", help="Where I searech for subtitles")
        parser.add_argument("--recursive_search", action="store_true", help="Do I search your directory recursively?")
        parser.add_argument("--save_at", help="Only the saving directory. Do not include file name!")
        parser.add_argument("--file_name", help="Only the saved file's name. Do not include directory")
        parser.add_argument("--lang", choices=["en", "fa", "fr"], help= "Choose a language: en, fr, fa")
        parser.add_argument("--phrase", help="What to look for")
        parser.add_argument("--margin_in_milliseconds", type=int, help="How much to cut out of the video, before and after")

        return parser

    # Public
    # --------------------------------

    def parse_args(self, args: list=None):
        if args is None:
            self.__args = self.__parser.parse_args()
        else:
            self.__args = self.__parser.parse_args(args)
        return self.__args
    
    def print_help(self) -> None:
        self.__args.print_help()

    def get_args(self) -> dict:
        if self.__args is None:
            raise RuntimeError("Arguments not parsed yet.")
        return {"use_regex": self.__args.use_regex,
                "lang": self.__args.lang,
                "directory": self.__args.directory,
                "recursive_search": self.__args.recursive_search,
                "phrase": self.__args.phrase,
                "start": self.__args.start,
                "end": self.__args.end,
                "save_at": self.__args.save_at,
                "file_name": self.__args.file_name,
                "random": self.__args.random,
                "margin_in_milliseconds": self.__args.margin_in_milliseconds}
    
    @classmethod
    def dict_to_list(cls, dictionary: dict) -> list[str]:
        args_list: list[str] = []
        for key, value in dictionary.items():
             if isinstance(value, bool):
                if value:
                    args_list.append(f"--{key}")
             else:
                args_list.extend([f"--{key}", str(value)])
        return args_list


    ## Getters
    ## --------------------------------

    @property
    def save_at(self) -> str: return self.__args.save_at
    
    @property
    def directory(self) -> str: return self.__args.directory

    @property
    def recursive_search(self) -> bool: return self.__args.recursive_search

    @property
    def use_regex(self) -> bool: return self.__args.use_regex

    @property
    def start(self) -> bool: return self.__args.start

    @property
    def end(self) -> bool: return self.__args.end

    @property
    def lang(self) -> str: return self.__args.lang

    @property
    def phrase(self) -> str: return self.__args.phrase

    @property
    def file_name(self) -> str: return self.__args.file_name

    @property
    def select_random(self) -> bool: return self.__args.random

    @property
    def margin_in_milliseconds(self) -> int: return self.__args.margin_in_milliseconds