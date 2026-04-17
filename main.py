from colors import *
from assessments import pressure_assessment, cardiac_assessment, diabetes_assessment
from getpass import getpass
from dataclasses import dataclass
from user import State, load


def ask(question: str, options: list[str], cancel: bool = False) -> int:
    while True:
        print(
            f"{CYAN}{question} (Press the number in front of the option and press ENTER.){RESET_ALL}"
        )
        if cancel:
            print(f"  {YELLOW}0.) Cancel{RESET_ALL}")
        for i, opt in enumerate(options):
            print(f"  {YELLOW}{i + 1}.) {GREEN}{opt}{RESET_ALL}")

        try:
            if int(not cancel) <= (o := int(input("> "))) < len(options) + 1:
                return o
            else:
                print(f"{RED}Please select an available option!{RESET_ALL}")
                continue
        except ValueError:
            print(f"{RED}Please select an available option!{RESET_ALL}")
            continue


def main():
    print(f"{BRIGHT}{BOLD}{BLUE}Welcome to {GREEN}{UNDERLINE}HeartBuddy{RESET_ALL}")
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
                    print(f"{GREEN}Signed up.{RESET_ALL}")
                    state.logged_in = user
                elif c == 2:
                    if user := state.login(username, password):
                        print(f"{GREEN}Logged in!{RESET_ALL}")
                        state.logged_in = user
                    else:
                        print(f"{RED}Wrong username or password!{RESET_ALL}")

    while True:
        match ask(
            "What is your primary concern?",
            ["Blood Pressure", "Cardiac Risks", "Diabetes"],
            cancel=True,
        ):
            case 0:
                print(f"{GREEN}Goodbye!{RESET_ALL}")
                break
            case 1:
                print(f"{GREEN}Assessing {UNDERLINE}{RED}Blood Pressure{RESET_ALL}")
                sys = float(input(f"{YELLOW}Systolic  (mmHg):{RESET_ALL} "))
                dia = float(input(f"{YELLOW}Diastolic (mmHg):{RESET_ALL} "))
                age = float(input(f"{YELLOW}Age:{RESET_ALL} "))
                pressure_assessment(sys, dia, age)
            case 2:
                print(f"{GREEN}Assessing {UNDERLINE}{RED}Cardiac Risks{RESET_ALL}")
                ldl = float(input(f"{YELLOW}LDL (mg/dL):{RESET_ALL} "))
                hdl = float(input(f"{YELLOW}HDL (mg/dL):{RESET_ALL} "))
                cardiac_assessment(ldl, hdl)
            case 3:
                print(f"{GREEN}Assessing {UNDERLINE}{YELLOW}Diabetes{RESET_ALL}")
                hba1c = float(input(f"{YELLOW}HbA1C:{RESET_ALL} "))
                diabetes_assessment(hba1c)

    state.save()


if __name__ == "__main__":
    main()
