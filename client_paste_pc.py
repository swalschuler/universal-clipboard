#! python3
# Client for universal clipboard

import requests
import pyperclip
from win10toast import ToastNotifier

r = requests.get("http://antman99781.pythonanywhere.com/clipboard")
pyperclip.copy(r.text)

toaster = ToastNotifier()
toaster.show_toast("Universal Clipboard", "Grabbed the value: " + r.text)