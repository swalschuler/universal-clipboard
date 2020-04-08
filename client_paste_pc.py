#! python3
# Client for universal clipboard

import requests
import pyperclip

r = requests.get("http://antman99781.pythonanywhere.com/clipboard")
pyperclip.copy(r.text)
