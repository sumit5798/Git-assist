import subprocess

def perform_git_log():
    try:
        log_output = subprocess.check_output(["git", "log"]).decode("utf-8")
        print("Git log:\n", log_output)
    except subprocess.CalledProcessError as e:
        print("Error during Git log retrieval:", e)
