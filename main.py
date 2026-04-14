from dataclasses import dataclass
from user import load, save
import sqlite3
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

BOLD = "\033[1m"
UNDERLINE = "\033[4m"


def main():
    colorama_init(autoreset=True)

    print(
        f"{Style.BRIGHT}{BOLD}{Fore.BLUE}Welcome to {Fore.GREEN}{UNDERLINE}HeartBuddy"
    )
    state = load()

    save(state)


if __name__ == "__main__":
    main()
