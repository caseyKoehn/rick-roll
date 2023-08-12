import subprocess
import webbrowser
import platform
import time

mess = "You've been rickrolled!"
name = "Casey Koehn"
website = "https://digitalcoffeecup.com"
contact = "email_here"
job_title = "Python - Flutter Dev"
github = "https://github.com/caseyKoehn/rick-roll"
space = "\n\n"
message = mess + space + name + space + job_title + space + website + space + contact + space + github

try:
    import keyboard
    print("The library is installed.")

except ImportError:
    command = "pip install keyboard"
    print("The library is not installed.")

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("Error executing the command:", e)

webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
webbrowser.open(website)
webbrowser.open("https://github.com/caseyKoehn/rick-roll")

def open_text_editor():
    if platform.system() == "Windows":
        subprocess.run(["start", "/max", "notepad"], shell=True, text=True)
    elif platform.system() == "Darwin":
        subprocess.run(["open", "-e"])
    else:
        subprocess.run(["xdg-open"])

open_text_editor()

time.sleep(2)

keyboard.write(message)
