import webbrowser
import time
import subprocess

import main
import recognize_voice
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import pop_up_window


def url_finder(input_func):
    query = input_func.replace(' ', '+')

    # search for the best similar matching video
    url = 'https://www.youtube.com/results?search_query=' + query
    source_code = requests.get(url, timeout=1)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    # fetches the url of the video
    songs = soup.findAll('div', {'class': 'yt-lockup-video'})
    if len(songs) <= 0:
        url = 'https://www.youtube.com/results?search_query=' + query
        source_code = requests.get(url, timeout=1)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        # fetches the url of the video
        songs = soup.findAll('div', {'class': 'yt-lockup-video'})

    song = songs[0].contents[0].contents[0].contents[0]
    try:
        link = song['href']
        return link
    except KeyError:
        print("Can't find any song,check your network or try a new word")
        return "error"


def youtube_query_handler():
    main.speak("Sir what do u want to watch in youtube")
    flag = 1
    while flag:
        search_request = recognize_voice.listen_command().lower()

        if "cancel" not in search_request and "null" not in search_request and "no" not in search_request:
            # this blocks executes when a user tries to search about some information details in wikipedia
            main.speak("Opening youtube and searching for your request")
            search_request = search_request.replace(' ', '+')
            url = url_finder(search_request)
            webbrowser.open("https://www.youtube.com/" + url)
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
                    pop_up_window.pop_up_msg("YouTube download window", "download has started", "sss")
                    print("https://www.youtube.com/" + url)
                    y = YouTube("https://www.youtube.com/" + url).streams.first().download("E:\\movies")
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


if __name__ == '__main__':
    # url_finder("Avengers infinity war movie")
    youtube_query_handler()
