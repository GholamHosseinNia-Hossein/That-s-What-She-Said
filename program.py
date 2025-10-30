from phrase_instance import Phrase_Instance
from prompt import Prompt
from sub_handler import Sub_Handler
from settings import Settings
import shlex

def main():
    prompt = set_prompt()

    while True:
        try:
            entered_data = prompt.parse_args(shlex.split(input("> ")))
            if entered_data.start:
                break
            Settings.set_settings(prompt.get_args())
        except Exception as e:
            print ("Argument parsing failed!", e)

    
    if fit_for_output(prompt):
        output(prompt)

def set_prompt() -> Prompt:
    prompt = Prompt()
    prompt.print_help()
    prompt.parse_args(Prompt.dict_to_list(Settings.get_settings()))
    return prompt

def output(args: Prompt):
    sub_handler = Sub_Handler()
    # As of now, the application cannot search the subtitles embedded inside a video
    phrase_instances = sub_handler.find_instances(args.phrase, args.directory, args.recursive_search, False, args.use_regex)
    if len(phrase_instances) < 1:
        args.add("Not Found")
    else:
        # Print the output for now
        # save_as(phrase_instances)
        for instance in phrase_instances:
            print(f"FILE: {instance.file_path}, \t {instance.start_time}-{instance.end_time}")
            print(f"PHRASE: {instance.phrase}")
            print("-------------------------")

# Not yet developed. Waiting for the CS50 AI course...
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

def exit_if_unable(args: dict):
    # Check if the args are able to be used
    # Check if the args are able to be used in the program
    # Check if the args are able to be used in the function
    # Check if the args are able to be used in the class
    pass


if __name__ == "__main__":
    main()