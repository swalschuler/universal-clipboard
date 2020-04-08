#! python3
# Client for universal clipboard
# 
# #>>> r = requests.get("http://antman99781.pythonanywhere.com/clipboard")
#>>> r.text
#'bob\n'
#>>>

import requests
import pyperclip

payload = {'value': pyperclip.paste()}
r = requests.post("http://antman99781.pythonanywhere.com/clipboard", data=payload)
