from process_command import *
from recognizeVoice import *
from git_commit import *
from git_log import *

def main():
    recognized_text = recognize_voice()
    print("You said:", recognized_text)

    verb = process_command(recognized_text)
    
    if verb == "commit":
        commit_message = extract_commit_message(recognized_text)
        perform_git_commit(commit_message)
    elif verb == "log":
        perform_git_log()
    else:
        print("Unrecognized command:", verb)

if __name__ == "__main__":
    main()
