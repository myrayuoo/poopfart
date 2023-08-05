import os

class CleanUp():

    def __init__(self):
        self.app_data = os.getenv("LOCALAPPDATA")
        self.cleanup()

    def cleanup(self):
        """
        Removes all trace
        of poopfart by deleting
        log files left by
        poopfart.
        """
        poopfart_dir = os.path.join(self.app_data, "poopfart")
        for file in os.listdir(poopfart_dir):
            os.remove(os.path.join(poopfart_dir, file))
        os.rmdir(poopfart_dir)
        os.remove(os.path.join(self.app_data, f'poopfart-[{os.getlogin()}].zip'))
