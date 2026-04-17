from user import State, load
from colorama import Fore  # type: ignore[import-untyped]
from colorama import Style


def pressure_assessment(sys: float, dia: float, age: float):
    if age < 40:
        if sys > 140 or dia > 90:
            sys_diag = f"{Fore.RED}High"
        elif sys > 120 or dia > 80:
            sys_diag = f"{Fore.YELLOW}Elevated"
        else:
            sys_diag = f"{Fore.GREEN}Normal"

    elif age < 60:
        if sys > 150 or dia > 95:
            sys_diag = f"{Fore.RED}High"
        elif sys > 130 or dia > 85:
            sys_diag = f"{Fore.YELLOW}Elevated"
        else:
            sys_diag = f"{Fore.GREEN}Normal"

    else:
        if sys > 160 or dia > 100:
            sys_diag = f"{Fore.RED}High"
        elif sys > 140 or dia > 90:
            sys_diag = f"{Fore.YELLOW}Elevated"
        else:
            sys_diag = f"{Fore.GREEN}Normal"

    if dia < 60:
        dia_diag = f"{Fore.CYAN}Low"
    elif dia <= 80:
        dia_diag = f"{Fore.GREEN}Normal"
    elif dia <= 90:
        dia_diag = f"{Fore.YELLOW}Elevated"
    else:
        dia_diag = f"{Fore.RED}High"

    handle_bp()
    print(f"Systolic:  {sys_diag}{Style.RESET_ALL} ({sys} mmHg)")
    print(f"Diastolic: {dia_diag}{Style.RESET_ALL} ({dia} mmHg)")


def cardiac_assessment(ldl: float, hdl: float):
    if ldl > 160.0:
        handle_ca()
        ldl_diag = f"{Fore.RED}High"
    elif ldl > 100.0:
        ldl_diag = f"{Fore.YELLOW}Elevated"
    else:
        ldl_diag = f"{Fore.GREEN}Normal"

    if hdl >= 60.0:
        handle_ca()
        hdl_diag = f"{Fore.RED}High"
    elif 50.0 <= hdl < 60.0:
        hdl_diag = f"{Fore.GREEN}Normal"
    elif 40.0 <= hdl < 50.0:
        hdl_diag = (
            f"{Fore.CYAN}Low for Women{Style.RESET_ALL}, {Fore.GREEN}Normal for Men"
        )
    else:
        hdl_diag = f"{Fore.CYAN}Low"

    print(f"LDL: {ldl_diag} ({ldl} mg/dL)")
    print(f"HDL: {hdl_diag} ({hdl} mg/dL)")


def diabetes_assessment(hba1c: float):
    if hba1c > 6.4:
        handle_diabetes()
    elif 5.7 < hba1c <= 6.4:
        print(f"{Fore.YELLOW}You have pre-diabetes. Be careful,,,,")
    else:
        print(f"{Fore.GREEN}Your HBA1C is normal!")


def handle_bp():
    print(f"{Fore.RED}Referred to the correspondent department")


def handle_ca():
    print(f"{Fore.RED}Referred to the correspondent department")


def handle_diabetes():
    print(f"{Fore.RED}Referred to the correspondent department")
