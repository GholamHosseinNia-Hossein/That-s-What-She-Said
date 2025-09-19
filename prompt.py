import sys
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

    def parse_args() -> dict:
        # Receives arguments from the command line & Parses them
        # Updates the __args variable
        # Returns the recieved data
        pass

    def print_help(self) -> None:
        self.__args.print_help()

    def command_line_args(self) -> None:
        # User may call it once, at the beginning of the program
        pass

    def get_args(self) -> dict:
        # Returns all the entered arguments as a dictionary
        pass

    ## Getters
    ## --------------------------------

    @property
    def save_path(self) -> str:
        pass
    
    @property
    def video_directory(self) -> str:
        pass

    @property
    def sub_collection_directory(self) -> str:
        pass

    @property
    def instance_number(self) -> int:
        pass
    