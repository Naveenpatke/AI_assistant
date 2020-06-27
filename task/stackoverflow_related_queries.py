import time
import webbrowser
import pyperclip

import main
import recognize_voice


def stackoverflow_query_handler():
    main.speak("sir what do you want to search in stack overflow")
    main.speak("or should i copy the text which you have previously copied to ur clipboard")
    flag = 1
    while flag:
        search_request = recognize_voice.listen_command().lower()

        if "clip board" in search_request or "clipboard" in search_request:
            # this blocks executes when a user tries to search about some information details in wikipedia
            clipboard_data = pyperclip.paste()
            webbrowser.open("https://stackoverflow.com/search?q=" + clipboard_data)
            time.sleep(4)
            main.speak("This is what i found in stack overflow sir")
            flag = 0

        elif "cancel" in search_request or "no" in search_request:
            # this block executes when a user request to open stack overflow but denies to search in stack overflow
            flag = 0
            main.speak("As you wish sir")

        elif "null" in search_request:
            # this block executes when a user didn't provide any command after requesting maggi to open stack overflow
            pass

        else:
            # this block executes when the user commands to search his request in google
            webbrowser.open("https://stackoverflow.com/search?q=" + search_request)
            time.sleep(4)
            main.speak("This is what i found in stack overflow sir")
            time.sleep(4)
            main.speak("Do you want to search anything else in stack overflow?")
            response = recognize_voice.listen_command().lower()

            if "no" in response:
                # to terminate the loop from being asked to user to search anything else in stack overflow
                flag = 0
            else:
                pass
