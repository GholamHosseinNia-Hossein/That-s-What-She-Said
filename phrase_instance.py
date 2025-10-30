from datetime import time

class Phrase_Instance:
    
    def __init__(self, path=None, start=None, end=None, phrase=None, sub_number=-1):
        self._file_path: str = path
        self._start_time: time = start
        self._end_time: time = end
        self._sub_number: int = sub_number # Only if we're dealing with a subtitle attached to a video
        self._phrase: str = phrase

    @property
    def file_path(self) -> str: return self._file_path

    @file_path.setter
    def file_path(self, path: str): self._file_path = path
    
    @property
    def start_time(self) -> time: return self._start_time

    @start_time.setter
    def start_time(self, time: time): self._start_time = time

    @property
    def end_time(self) -> time: return self._end_time

    @end_time.setter
    def end_time(self, time: time): self._end_time = time

    @property
    def phrase(self) -> str: return self._phrase
    
    @phrase.setter
    def phrase(self, phrase: str): self._phrase = phrase

    # For mkv files with several subtitles.
    # This property is tentative and may be subject to change.
    @property
    def sub_number(self) -> int: return self._sub_number

    @sub_number.setter
    def sub_number(self, number: int): self._sub_number = number