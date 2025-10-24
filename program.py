from phrase_instance import Phrase_Instance
from prompt import Prompt
from sub_handler import Sub_Handler
from settings import Settings


def main():
    prompt = set_prompt()

    while True:
        entered_data = prompt.parse_args()
        if entered_data["exit"]:
            break
        Settings.set_settings(entered_data)
    
    if fit_for_output(prompt):
        output(prompt)
    finalize(Settings, prompt)

def set_prompt() -> Prompt:
    prompt = Prompt()
    prompt.print_help()
    
    # fill prompt from settings
    for key, value in Settings.get_settings():
        prompt._args[key] = value


def output(args: Prompt):
    sub_handler = Sub_Handler()
    # As of now, the application cannot search the subtitles embedded inside a video
    phrase_instances = sub_handler.find_instances(args.phrase, args.directory, args.recursive_search, False, args.use_regex)
    if phrase_instances is None:
        args.add("Not Found")
    else:
        # Print the output for now
        # save_as(phrase_instances)
        for instance in phrase_instances:
            print(f"FILE: {instance.file_path}, \t {instance.start_time}-{instance.end_time}")
            print(f"PHRASE: {instance.phrase}")
            print(f"-------------------------")

def save_as(phrase_instance: Phrase_Instance):
    # You've got the subtitle address
    # You've got the output address
    # You may have the video address, if not, save it as 'srt'
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
    return True

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