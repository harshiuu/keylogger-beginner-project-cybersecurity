# Keylogger project using python


Welcome to **Keylogger project using python**, a simple and educational project demonstrating how to capture and log keystrokes in Python. 

> **Note:** This project is intended for educational purposes only. Make sure you have permission before running keyloggers on any system that’s not yours.

---

## 📜 Table of Contents

- [Overview](#-overview)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Legal Notice ⚠️](#-legal-notice-️)
- [Screenshots](#-screenshots)
- [License](#-license)
- [Contributing](#-contributing)
- [Contact](#-contact)

---

## 🧐 Overview

This **Python Keylogger** logs keystrokes into a text file and runs quietly in the background. It's built with minimal code, using the [`pynput`](https://pypi.org/project/pynput/) library to monitor keyboard inputs. This project helps in understanding how keyloggers work and how you can build one for personal use—debugging your own keyboard input or monitoring personal device activity.

---

## ⚙️ Installation

To run this keylogger on your local machine, follow the steps below:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/harshiuu/keylogger-beginner-project-cybersecurity
    ```

2. **Install the dependencies**:

    ```bash
    pip install pynput
    ```

3. **Run the script**:

    ```bash
    python keylogger.py
    ```

---

## 🎯 Usage

Once the script is executed, the keylogger will begin recording key presses and store them in `key_log.txt`.

1. Open the terminal and navigate to the folder containing `keylogger.py`.
2. Run the script and start typing in any text editor or browser.
3. The keystrokes will be logged in the file `key_log.txt`.

---

## 🔍 How It Works

The keylogger uses the `pynput` library to listen for keyboard events. It captures each keystroke and appends it to a log file. Here's a breakdown:

- **Key Presses**: Logs every key typed, whether alphanumeric or special keys (like Shift or Enter).
- **Log Storage**: The data is stored in a text file called `key_log.txt` located in the project directory.

---

## ⚖️ Legal Notice ⚠️

Keyloggers have ethical and legal implications. Make sure to only use this software for personal, non-malicious purposes. Logging keystrokes without permission on someone else’s computer is illegal in many jurisdictions.

---

## 🖼️ Screenshots

Here are some screenshots demonstrating the keylogger in action:

### Keylogger in Terminal (i have already installed it)
![pip install](https://github.com/user-attachments/assets/916a1862-19f9-4522-8880-d2c14a072d42)




### Running and testing
![2](https://github.com/user-attachments/assets/f18f61c3-dac2-4bfe-b625-2694146ba57f)
![3](https://github.com/user-attachments/assets/392dd605-a645-4b84-99ce-7c0ac71ccb31)




### Log File Output
![final out](https://github.com/user-attachments/assets/7b4e530f-ad01-42ce-99e8-1ec4d09c7444)


---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

If you'd like to contribute, feel free to submit a pull request or open an issue to discuss potential improvements.

---

## 📧 Contact

Feel free to reach out with any questions or feedback!

- GitHub: [@harshiuu](https://github.com/harshiuu)
- Linkedin: [@harshitnimbhore](https://www.linkedin.com/in/harshit-nimbhore-215187229/)

---

### 🔗 References

- [`pynput`](https://pypi.org/project/pynput/) — The library used for listening to keyboard events.

