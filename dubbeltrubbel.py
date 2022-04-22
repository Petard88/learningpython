from pynput import keyboard

keyboard = Controller()

def on_press(key):
    if key == keyboard.Key.shift:
        keyboard.t
    else:
        print(key)
if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()