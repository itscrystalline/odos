from colors import *
from user import State, load


def pressure_assessment(sys: float, dia: float, age: float):
    if age < 40:
        if sys > 140 or dia > 90:
            handle_bp()
            sys_diag = f"{RED}High{RESET_ALL}"
        elif sys > 120 or dia > 80:
            handle_bp()
            sys_diag = f"{YELLOW}Elevated{RESET_ALL}"
        else:
            sys_diag = f"{GREEN}Normal{RESET_ALL}"

    elif age < 60:
        if sys > 150 or dia > 95:
            handle_bp()
            sys_diag = f"{RED}High{RESET_ALL}"
        elif sys > 130 or dia > 85:
            handle_bp()
            sys_diag = f"{YELLOW}Elevated{RESET_ALL}"
        else:
            sys_diag = f"{GREEN}Normal{RESET_ALL}"

    else:
        if sys > 160 or dia > 100:
            handle_bp()
            sys_diag = f"{RED}High{RESET_ALL}"
        elif sys > 140 or dia > 90:
            handle_bp()
            sys_diag = f"{YELLOW}Elevated{RESET_ALL}"
        else:
            sys_diag = f"{GREEN}Normal{RESET_ALL}"

    if dia < 60:
        handle_bp()
        dia_diag = f"{CYAN}Low{RESET_ALL}"
    elif dia <= 80:
        dia_diag = f"{GREEN}Normal{RESET_ALL}"
    elif dia <= 90:
        handle_bp()
        dia_diag = f"{YELLOW}Elevated{RESET_ALL}"
    else:
        handle_bp()
        dia_diag = f"{RED}High{RESET_ALL}"

    print(f"Systolic:  {sys_diag}{RESET_ALL} ({sys} mmHg)")
    print(f"Diastolic: {dia_diag}{RESET_ALL} ({dia} mmHg)")


def cardiac_assessment(ldl: float, hdl: float):
    if ldl > 160.0:
        handle_ca()
        ldl_diag = f"{RED}High{RESET_ALL}"
    elif ldl > 100.0:
        ldl_diag = f"{YELLOW}Elevated{RESET_ALL}"
    else:
        ldl_diag = f"{GREEN}Normal{RESET_ALL}"

    if hdl >= 60.0:
        handle_ca()
        hdl_diag = f"{RED}High{RESET_ALL}"
    elif 50.0 <= hdl < 60.0:
        hdl_diag = f"{GREEN}Normal{RESET_ALL}"
    elif 40.0 <= hdl < 50.0:
        hdl_diag = f"{CYAN}Low for Women{RESET_ALL}, {GREEN}Normal for Men{RESET_ALL}"
    else:
        handle_bp()
        hdl_diag = f"{CYAN}Low{RESET_ALL}"

    print(f"LDL: {ldl_diag} ({ldl} mg/dL)")
    print(f"HDL: {hdl_diag} ({hdl} mg/dL)")


def diabetes_assessment(hba1c: float):
    if hba1c > 6.4:
        handle_diabetes()
    elif 5.7 < hba1c <= 6.4:
        print(f"{YELLOW}You have pre-diabetes. Be careful,,,,{RESET_ALL}")
    else:
        print(f"{GREEN}Your HBA1C is normal!{RESET_ALL}")


def handle_bp():
    print(f"{RED}Referred to the correspondent department{RESET_ALL}")


def handle_ca():
    print(f"{RED}Referred to the correspondent department{RESET_ALL}")


def handle_diabetes():
    print(f"{RED}Referred to the correspondent department{RESET_ALL}")
