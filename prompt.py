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
        parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
        parser.add_argument("-q", "--quiet", action="store_true", help="Enable quiet output")
        parser.add_argument("-s", "--start", action="store_true", help="Start the clipping procedure")
        parser.add_argument("-e", "--end", action="store_true", help="End the program")
        return parser

    # Public
    # --------------------------------

    def parse_args() -> None:
        # Receives arguments from the command line & Parses them
        # Updates the __args variable
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
    