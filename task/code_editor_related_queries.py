import subprocess
import webbrowser
import time

import main
import recognize_voice


def request_command(toggle):
    if toggle == 1:
        main.speak("opening editor")
    time.sleep(5)
    main.speak("Sir do you need any other help sir")


def code_editor_query_handler(query):
    try:
        if "notepad" in query:
            subprocess.Popen(['Notepad.exe'])
            request_command(1)

        elif "visual studio code " in query or "visual studio" in query:
            subprocess.Popen(['D:\\Installedsoftware\\VisualStudio\\Microsoft VS Code\\Code.exe'])
            request_command(1)

        elif "codeblocks" in query or "code blocks" in query:
            subprocess.Popen(['D:\\Installedsoftware\\CodeBlocks\\codeblocks.exe'])
            request_command(1)

        else:
            raise FileNotFoundError()

    except FileNotFoundError:
        main.speak("The system cannot find the editor you specified," +
                   " would u like me to search about the editor in google")
        sub_query = recognize_voice.listen_command().lower()
        query += " download"
        query = query.replace(' ', '+')
        while True:
            if "yes" in sub_query:
                main.speak("Searching your request in google")
                webbrowser.open("https://google.com/search?q=" + query)
                time.sleep(4)
                main.speak("This is what i found in google, You can download the editor from here")
                request_command(0)
                break

            elif "no" in sub_query:
                break
    return
