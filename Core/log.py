import datetime
from colorama import Fore, init
init(autoreset=True)


class logging:
    @classmethod
    def log_message(self, level:str, level_color:str, message:str):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}{current_time}{Fore.WHITE}] {Fore.WHITE}[{level_color}{level}{Fore.WHITE}] {message}{Fore.RESET}")
    
    @classmethod
    def info(self, message:str):
        self.log_message("INFO", Fore.LIGHTGREEN_EX, message)
    
    @classmethod
    def warning(self, message:str):
        self.log_message("WARNING", Fore.LIGHTYELLOW_EX, message)
    
    @classmethod
    def error(self, message:str):
        self.log_message("ERROR", Fore.LIGHTRED_EX, message)