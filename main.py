from assessments import pressure_assessment, cardiac_assessment, diabetes_assessment
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
    while True:
        print(
            f"{Fore.CYAN}{question} (Press the number in front of the option and press ENTER.)"
        )
        if cancel:
            print(f"  {Fore.YELLOW}0.) Cancel")
        for i, opt in enumerate(options):
            print(f"  {Fore.YELLOW}{i + 1}.) {Fore.GREEN}{opt}")

        try:
            if (
                int(not cancel)
                <= (o := int(input("> ")))
                < (len(options) + int(cancel))
            ):
                return o
            else:
                print(f"{Fore.RED}Please select an available option!")
                continue
        except:
            print(f"{Fore.RED}Please select an available option!")
            continue


def main():
    colorama_init(autoreset=True)

    print(
        f"{Style.BRIGHT}{BOLD}{Fore.BLUE}Welcome to {Fore.GREEN}{UNDERLINE}HeartBuddy"
    )
    state = load()

    while not state.logged_in:
        match ask(
            "Do you want to Sign up or Log in?", ["Sign Up", "Log In"], cancel=True
        ):
            case 0:
                return
            case 1 | 2 as c:
                username = input("Username: ")
                password = getpass("Password (will not show): ")
                if c == 1:
                    user = state.signup(username, password)
                    print(f"{Fore.GREEN}Signed up.")
                    state.logged_in = user
                elif c == 2:
                    if user := state.login(username, password):
                        print(f"{Fore.GREEN}Logged in!")
                        state.logged_in = user
                    else:
                        print(f"{Fore.RED}Wrong username or password!")

    match ask(
        "What is your primary concern?", ["Blood Pressure", "Cardiac Risks", "Diabetes"]
    ):
        case 1:
            print(f"{Fore.GREEN}Assessing {UNDERLINE}{Fore.RED}Blood Pressure")
            sys = float(input(f"{Fore.YELLOW}Systolic  (mmHg):{Style.RESET_ALL} "))
            dia = float(input(f"{Fore.YELLOW}Diastolic (mmHg):{Style.RESET_ALL} "))
            age = float(input(f"{Fore.YELLOW}Age:{Style.RESET_ALL} "))
            pressure_assessment(sys, dia, age)
        case 2:
            print(f"{Fore.GREEN}Assessing {UNDERLINE}{Fore.RED}Cardiac Risks")
            ldl = float(input(f"{Fore.YELLOW}LDL (mg/dL):{Style.RESET_ALL} "))
            hdl = float(input(f"{Fore.YELLOW}HDL (mg/dL):{Style.RESET_ALL} "))
            cardiac_assessment(ldl, hdl)
        case 3:
            print(f"{Fore.GREEN}Assessing {UNDERLINE}{Fore.YELLOW}Diabetes")
            hba1c = float(input(f"{Fore.YELLOW}HbA1C:{Style.RESET_ALL} "))
            diabetes_assessment(hba1c)

    state.save()


if __name__ == "__main__":
    main()
