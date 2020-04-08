#! python3
# Client for universal clipboard

import requests
import pyperclip
from win10toast import ToastNotifier

text = pyperclip.paste()
payload = {'value': text}
r = requests.post("http://antman99781.pythonanywhere.com/clipboard", data=payload)

toaster = ToastNotifier()
toaster.show_toast("Universal Clipboard", "Placed the value: " + text)