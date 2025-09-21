from datetime import time

class Phrase_Instance:
    
    def __init__(self):
        self._file_path: str = None
        self._start_time: time = None
        self._end_time: time = None
        self._sub_number: int = -1 # Only if we're dealing with a subtitle attached to a video

    @property
    def file_path(self) -> str: self._file_path

    @file_path.setter
    def file_path(self, path: str): self._file_path = path
    
    @property
    def start_time(self) -> time: self._start_time

    @start_time.setter
    def start_time(self, time: time): self._start_time = time

    @property
    def end_time(self) -> time: self._end_time

    @end_time.setter
    def end_time(self, time: time): self._end_time = time

    @property
    def sub_number(self) -> int: self._sub_number

    @sub_number.setter
    def sub_number(self, number: int): self._sub_number = number