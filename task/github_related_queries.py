from github import Github
import webbrowser
import time

import environment_var
import recognize_voice
import main


def github_query():
    g = Github(environment_var.access_token)
    main.speak("Sir what do u want to watch in github")
    flag = 1
    while flag:
        search_request = recognize_voice.listen_command().lower()

        if "cancel" not in search_request and "null" not in search_request and "no" not in search_request:
            # this blocks executes when a user tries to search about some information details in wikipedia
            main.speak("Opening youtube and searching for your request")
            search_request = search_request.replace(' ', '+')
            # webbrowser.open("https://www.youtube.com/" + url)
            time.sleep(4)
            main.speak("This is what i found in youtube sir")
            time.sleep(2)
            flag1 = 1
            main.speak("Do you want to download this video sir?")
            while flag1:
                response = recognize_voice.listen_command().lower()

                if "no" in response:
                    # to terminate the loop from being asked to user to search anything else in youtube
                    flag1 = 0
                    flag = 0
                elif "yes" in response or "sure" in response or "download" in response:
                    main.speak("Initializing download")
                    # main.speak("Sir download has started, u can redirect to the download folder by clicking on the given link")
                    # pop_up_window.pop_up_msg("YouTube download window", "download has started", "sss")
                    # y = YouTube("https://www.youtube.com/" + url).streams.first().download("E:\\movies")
                    flag1 = 0
                    flag = 0
                else:
                    pass

        elif "cancel" in search_request or "no" in search_request:
            # this block executes when a user request to open youtube but denies to search in youtube
            flag = 0
            main.speak("As you wish sir")

        elif "null" in search_request:
            # this block executes when a user didn't provide any command after requesting maggi to open youtube
            pass


def github_query_handler():
    g = Github(environment_var.access_token)
    main.speak("Sir what are you looking for, Do u need any assistance")
    sub_query = recognize_voice.listen_command().lower()
    if "yes" in sub_query:
        main.speak("How can i help you sir")
        sub_query = recognize_voice.listen_command().lower()
        if "my repo" in sub_query:
            main.speak('Here are the details of all your repository')
            for repo in g.get_user().get_repos():
                main.speak("repository name"+repo)
                main.speak("description of the repo" + repo.description)
        elif "repo 1" in sub_query:
            repositories = g.search_repositories(query='language:python')
            for repo in repositories:
                print(repo)
    else:
        repositories = g.search_repositories(query='language:python')
        for repo in repositories:
            print(repo.clone_url)


def demo():
    g = Github(environment_var.access_token)
    repositories = g.search_repositories(query='language:python')
    for repo in repositories:
        print(repo)
        #print(repo.compare("awesome-python", "public-apis"))


if __name__ == '__main__':
    demo()
