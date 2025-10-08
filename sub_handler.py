from phrase_instance import Phrase_Instance
import datetime
import os
import re
import pysubs2

## Define local variables that contain 'regex', 'search_videos', 'directory', and 'phrase'
class Sub_Handler:
    
    _phrase: str = None
    _directory: str = None
    _regex: bool = True
    _search_videos: bool = False

    def __class_initialize():
        pass

    @classmethod
    def find_instances(cls, phrase: str, directory: str, search_recursive: bool = True, search_videos: bool = True, regex: bool = True) -> list[Phrase_Instance]:
        if not os.path.exists(directory) or os.path.isfile(directory):
            raise ValueError("Wrong directory path!")
        
        cls._regex = regex, cls._phrase = phrase, cls._directory = directory, cls._search_videos = search_videos

        if search_recursive:
            return cls._recursive_search(directory)
        else:
            return cls._normal_search(directory)


    @classmethod
    def cut_subtitle(cls, begin: datetime.time, duration: datetime.timedelta, save_as: str):
        pass

    @classmethod
    def set_start_time_as(cls, time: datetime.time):
        pass

    @classmethod
    def _recursive_search(cls, directory):
        instances: list[Phrase_Instance] = cls._normal_search(directory)
        for item in os.listdir(cls._directory):
            if os.path.isdir(os.path.isdir(item)):
                recursive_instances = cls._recursive_search(item) 
                if recursive_instances is not None: instances.append(recursive_instances)
        return instances

    @classmethod
    def _normal_search(cls, directory) -> list[Phrase_Instance]:
        instances : list[Phrase_Instance] = None
        for item in os.listdir(directory):
            path = os.path.join(directory, item)
            if os.path.isfile(path) and cls.is_subtitle(path):
                return cls.search_in_text(item, cls._regex, path[:-3])

    @classmethod                
    def is_subtitle(cls, path: str) -> bool:
        return True if path.endswith((".srt", ".vtt", ".ass", ".ssa")) else False
    
    # Problem No. 1:
    # Imagine you have a sentence splitted in two lines,
    # (which is actually quite common in subtitles)
    # This code cannot identify the phrase if it has been splitted
    @classmethod
    def search_in_text(cls, file: str, regex: bool, format: str) -> list[Phrase_Instance]:
        sub = pysubs2.load(file, encoding="utf-8")
        if regex:
            phrases = [line for line in sub if re.search(cls._phrase, line.text, re.IGNORECASE)]
        else:
            phrases = [line for line in sub if line.text.find(cls._phrase)]
        return phrases
    

Sub_Handler.__class_initialize()