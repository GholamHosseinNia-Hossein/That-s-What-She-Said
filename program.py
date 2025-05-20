from video import Video
from prompt import Prompt
from video_handler import VideoHandler
from subtitle_search import SubtitleSearch


def main():
    prompt = Prompt()
    while True:
        prompt.print_help()
        args = get_args()
        do_as_told(args)
        if args["quit"] or args["start"]:
            break
    
    if fit_for_output(args):
        output(args)
        report(args)
    else:
        report(args)

    finish()

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

def finish():
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