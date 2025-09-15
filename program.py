from video import Video
from prompt import Prompt
from video_handler import VideoHandler
from sub_searcher import SubSearcher
from settings import Settings


def main():
    settings = set_settigns()
    prompt = set_prompt()

    while True:
        args = prompt.get_args()
        if args["end"]:
            break
        settings.write_settings(args)
    
    if fit_for_output(args):
        output(args)
    report(args)
    finalize(settings, args)


def set_settigns() -> Settings:
    settings = Settings()
    settings.load_settings()
    if settings.is_empty():
        settings.fill_necessary_settings()
    return settings

def set_prompt() -> Prompt:
    prompt = Prompt()
    prompt.command_line_args()
    prompt.print_help()


def report(videos: list[Video], args: Prompt):
    pass

def output(args: Prompt):
    sub_handler = Sub_Handler()
    phrase_instances = sub_handler.search()
    if phrase_instances is None:
        args.add("Not Found")
    else:
        save_as(phrase_instances)

def save_as(phrase_instance: Phrase_Instance):
    # You've got the video address
    # You've got the subtitle address
    # You've got the output address
    # Come on! 
    pass

def get_videos():
    pass

def fit_for_output(args: dict) -> bool:
    # Check if the args are fit for output
    # Check if the args are valid
    # Check if the args are not empty
    # Check if the args are not None
    # Check if the args are not False
    # Check if the args are not 0
    # Check if the args are not ""
    # Check if the args are not []
    # Check if the args are not {}
    pass

def finalize():
    # Finish the program
    # Close all the files
    # Close all the connections
    # Close all the threads
    # Close all the processes
    # Close all the sockets
    # Close all the pipes
    # Close all the queues
    # Close all the locks
    # Close all the semaphores
    # Close all the events
    # Close all the timers
    pass

def exit_if_unable(args: dict):
    # Check if the args are able to be used
    # Check if the args are able to be used in the program
    # Check if the args are able to be used in the function
    # Check if the args are able to be used in the class
    pass


if __name__ == "main":
    main()