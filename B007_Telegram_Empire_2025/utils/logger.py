# utils/logger.py
from colorama import Fore, Style

class Logger:
    @staticmethod
    def b007(msg):
        print(f"{Fore.RED}{Style.BRIGHT}╔{'═'*70}╗")
        print(f"║ B 007 • {msg:<64} ║")
        print(f"╚{'═'*70}╝{Style.RESET_ALL}")

    @staticmethod
    def success(msg): Logger.b007(f"SUCCESS → {msg}")
    @staticmethod
    def error(msg): Logger.b007(f"ERROR → {msg}")
    @staticmethod
    def empire(msg): print(f"{Fore.MAGENTA}{Style.BRIGHT}★ B 007 EMPIRE ★ {msg} ★{Style.RESET_ALL}")