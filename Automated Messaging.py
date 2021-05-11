import time
import pyautogui


def send_message():
    time.sleep(5)
    text = open('Message.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')


send_message()
