import keyboard
keylogger = []
i = 0

def callback(x):
   keylogger.append(keyboard.read_key(suppress=True))
while True:
    keyboard.on_press(callback, suppress=False)
    if len(keylogger) == i + 2:
        print(keylogger[i])
        i = i + 2

