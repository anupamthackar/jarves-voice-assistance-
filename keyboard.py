from pynput.keyboard import Key,Controller

from time import sleep

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def backward():
    for i in range(10):
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        sleep(0.1)

def forward():
    for i in range(10):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        sleep(0.1)