from video import Video
from prompt import Prompt
from video_handler import VideoHandler
from subtitle_search import SubtitleSearch
from settings import Settings


def main():
    settings = Settings()
    settings.load_settings()
    prompt = Prompt()
    prompt.command_line_args()

    while True:
        if args["end"]:
            break
        args = get_args()
        settings.write_settings(args)
        prompt.print_help()
    
    if fit_for_output(args):
        output(args)
    report(args)
    finalize(settings, args)

def get_args() -> dict:
    # The user
    # Use Argparse to parse the arguments into a Prompt
    pass

def report(videos: list[Video], args: Prompt):
    pass

def output(args: Prompt):
    pass

def get_videos():
    pass

def do_as_told(args: dict):
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