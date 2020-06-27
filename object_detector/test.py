import cv2
import pytesseract
from gtts import gTTS
from PIL import Image
import time
from playsound import playsound


def text_detection_in_image():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    sample = 0
    toggle = 0
    time.sleep(2)
    while cap.isOpened():
        ret, img = cap.read()
        if ret:
            toggle = 1
            cv2.imshow('frame', img)
            cv2.imwrite('frame.png', img)
            cv2.waitKey(1)
            sample = sample + 1
        if sample == 2:
            sample = 0
            break

    cap.release()
    if toggle == 0:
        print('Camera is interrupted\nPlease execute the script again')
        cv2.destroyAllWindows()

    if toggle == 1:
        print('image is captured')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    im = Image.open("frame.png")
    text = pytesseract.image_to_string(gray, lang='eng')
    temp = text.encode('utf-8')
    print(text)
    ##############speak#####################
    lag = 'en'
    myobj = gTTS(text=text, lang=lag)
    myobj.save("test.mp3")
    playsound("test.mp3")
    ###########################################
    print(text)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    text_detection_in_image()
