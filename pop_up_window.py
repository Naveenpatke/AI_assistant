from tkinter import *
import webbrowser

from pytube import YouTube


def callback(url, root1):
    root1.destroy()  # to destroy the pop_up window
    webbrowser.open_new(url)


def status():
    video = YouTube("https://www.youtube.com/watch?v=MFX1wENYymA")
    video.register_on_progress_callback("none")


def pop_up_msg(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400  # popup window width
    h = 200  # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    # the below label is used to make a click able  link
    w = Label(root, text="Redirect to download folder", width=120, height=10, fg="blue", bg="black", cursor="hand2")
    w.pack()
    w.bind("<Button-1>", lambda e: callback("E:\movies", root))

    b = Button(root, text="OK", command=root.destroy, width=10, fg="blue", bg="black", )
    b.pack()

    # the below 3 lines of code is used to lift up the pop-up window in front of the current application
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    mainloop()


if __name__ == '__main__':
    pop_up_msg("Title goes here..", "Hello World!", "A path or second message can go here..")
    # hyper()
