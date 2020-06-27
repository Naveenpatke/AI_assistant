import wikipedia
import time
import webbrowser

import recognize_voice
import main


class NoResultFoundError(Exception):
    pass


def wikipedia_query_handler():
    main.speak("Sir what do you want to search in wikipedia...")
    flag = 1
    try:
        while flag:
            search_request = recognize_voice.listen_command().lower()

            if "cancel" not in search_request and "null" not in search_request:
                # this blocks executes when a user tries to search about some information details in wikipedia
                search_result = wikipedia.summary(search_request, sentences=2)
                main.speak("According to wikipedia")
                main.speak(search_result)
                time.sleep(4)
                main.speak("Do you want to search anything else in wikipedia?")
                response = recognize_voice.listen_command().lower()
                if "no" in response:
                    # to terminate the loop from being asked to user to search any else in wikipedia
                    flag = 0
                else:
                    main.speak("Sir what do you want to search in wikipedia...")

            elif "cancel" in search_request:
                # this block executes when a user request to open wikipedia but denies to search in wikipedia
                flag = 0
                main.speak("As you wish sir")

            elif "null" in search_request:
                # this block executes when a user didn't provide any command after requesting maggi to open wikipedia
                pass

            else:
                # this blocks executes when no result were found for the given command
                raise NoResultFoundError(search_request)

    except wikipedia.exceptions.PageError as e:
        main.speak("No result were found in wikipedia sir...")
        main.speak("sir you want me to search your request in google")
        sub_query = recognize_voice.listen_command().lower()
        while True:
            if "yes" in sub_query or "sure" in sub_query:
                # this block executes when the user wish to search his request in google
                webbrowser.open("https://google.com/search?q=" + str(e))
                break
            else:
                main.speak("Sir do you want me to search your request in google?")
                sub_query = recognize_voice.listen_command().lower()
    return
