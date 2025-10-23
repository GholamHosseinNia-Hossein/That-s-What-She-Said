from phrase_instance import Phrase_Instance
from prompt import Prompt
from sub_handler import Sub_Handler
from settings import Settings


def main():
    settings = set_settigns()
    prompt = set_prompt()

    while True:
        entered_data = prompt.parse_args()
        if entered_data["value"]:
            break
        settings.write_settings(entered_data)
    
    if fit_for_output(prompt):
        output(prompt)
    report(prompt)
    finalize(settings, prompt)


def set_settigns() -> Settings:
    settings = Settings()
    if settings.is_empty():
        settings.fill_necessary_settings()
    return settings

def set_prompt() -> Prompt:
    prompt = Prompt()
    prompt.command_line_args()
    prompt.print_help()

def output(args: Prompt):
    sub_handler = Sub_Handler()
    phrase_instances = sub_handler.search()
    if phrase_instances is None:
        args.add("Not Found")
    else:
        save_as(phrase_instances)

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