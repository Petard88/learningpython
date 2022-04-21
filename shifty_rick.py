import webbrowser
from pynput import keyboard


def on_press(key):
    if key == keyboard.Key.shift:
        webbrowser.open_new('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()