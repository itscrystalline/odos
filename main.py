from getpass import getpass
from dataclasses import dataclass
from user import State, load
import sqlite3

from colorama import init as colorama_init  # type: ignore[import-untyped]
from colorama import Fore
from colorama import Style

BOLD = "\033[1m"
UNDERLINE = "\033[4m"


def ask(question: str, options: list[str], cancel: bool = False) -> int:
    print(
        f"{Fore.CYAN}{question} (Press the number in front of the option and press ENTER.)"
    )
    if cancel:
        print(f"  {Fore.YELLOW}0.) Cancel")
    for i, opt in enumerate(options):
        print(f"  {Fore.YELLOW}{i + 1}.) {Fore.GREEN}{opt}")
    return int(input("> "))


def main():
    colorama_init(autoreset=True)

    print(
        f"{Style.BRIGHT}{BOLD}{Fore.BLUE}Welcome to {Fore.GREEN}{UNDERLINE}HeartBuddy"
    )
    state = load()

    match ask("Do you want to Sign up or Log in?", ["Sign Up", "Log In"], cancel=True):
        case 0:
            return
        case 1 | 2 as c:
            username = input("Username: ")
            password = getpass("Password (will not show): ")
            if c == 1:
                state.signup(username, password)
                print(f"{Fore.GREEN}Signed up.")
            elif c == 2:
                if state.login(username, password):
                    print(f"{Fore.GREEN}Logged in!")
                else:
                    print(f"{Fore.RED}Wrong username or password!")

    state.save()


if __name__ == "__main__":
    main()
