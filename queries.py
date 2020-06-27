import time
import os
import main
import recognize_voice
import image_to_text
from task import (github_related_queries, code_editor_related_queries, wikipedia_related_queries,
                youtube_related_queries, stackoverflow_related_queries, gmail_related_queries)

from object_detector import object_detector


def request_for_assistance(toggle):
    toggle = 1
    time.sleep(3)
    main.speak("Do you need any other help sir")


def activate_maggi(kernel):
    toggle = 0
    flag = 1
    while flag:
        if toggle == 0:
            main.speak("how can i help you")
        query = recognize_voice.listen_main_command().lower()

        if "don't" not in query and "no " not in query:
            print(query)

            if "wikipedia" in query:
                # this block executes when query related to wikipedia encounters
                wikipedia_related_queries.wikipedia_query_handler()
                request_for_assistance(toggle)

            elif "open youtube" in query:
                # this block executes when query related to youtube encounters
                youtube_related_queries.youtube_query_handler()
                request_for_assistance(toggle)

            elif "search stack overflow" in query or "stack overflow" in query or "open stack overflow" in query or "stackoverflow" in query:
                # this block executes when query related to stack overflow encounters
                stackoverflow_related_queries.stackoverflow_query_handler()
                request_for_assistance(toggle)

            elif "open github" in query or "github" in query:
                # this block executes when query related to github encounters
                github_related_queries.github_query_handler()
                request_for_assistance(toggle)

            elif "gmail" in query or "mail" in query or "send a mail" in query:
                # this block executes when query related to gmail encounters
                # gmail_related_queries.gmail_query_handler()
                request_for_assistance(toggle)

            elif "play music" in query:
                music_dir = "D:\\PERSONAL\\SONGS\\1 - Nenokkadine (2013)"
                files = os.listdir(music_dir)
                print(files)
                main.speak("Playing music")
                os.startfile(os.path.join(music_dir, files[1]))
                request_for_assistance(toggle)

            elif "detect text" in query:
                image_to_text.image_to_speech()

            elif "detect object" in query:
                # os.system(
                #     "python C:\\Users\\Naveen\\Desktop\\B-464object_detection\\" +
                #     "yolo-object-detection\\yolo_video.py --yolo yolo-coco"
                # )
                object_detector.object_detector()

            elif "editor" in query:
                print("edit")
                code_editor_related_queries.code_editor_query_handler(query)
                #request_for_assistance(toggle)

            elif "exit" in query or "terminate" in query:
                main.speak("Are you sure about it sir")
                sub_query = recognize_voice.listen_command().lower()
                flag = 1
                while flag:
                    if "yes" in sub_query or "sure" in sub_query:
                        main.speak("Executing termination protocol")
                        exit(0)
                    else:
                        toggle = 1
                        sub_query = recognize_voice.listen_command().lower()

            # elif "null" not in query:
            #     main.speak("Sir no results were found, should i search your request in google?")
            #     sub_query = recognize_voice.listen_command().lower()
            #     if "yes" in sub_query or "sure" in sub_query:
            #         webbrowser.open("https://google.com/search?q=" + query)
            #         time.sleep(4)
            #         main.speak("This is what i found in stack overflow sir")
            #         request_for_assistance(toggle)
            #     else:
            #         request_for_assistance(toggle)

            else:
                # kernel now ready for use
                if query not in "null":
                    query = query.upper()
                    maggi_speech = kernel.respond(query)
                    print("MAGGI: " + maggi_speech)
                    main.speak(maggi_speech)
                    toggle = 1

        else:
            main.speak("Sir if u need any help you can call me by just saying, Hey Maggi")
            flag = 0
