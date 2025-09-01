def readint(msg):
    try:
        n = int(input(msg))
    except (ValueError, TypeError):
        print("\033[31mInvalid input. Please enter an integer.\033[0m")
        return
    except KeyboardInterrupt:
        print("\n\033[33mInput cancelled by user.\033[0m")
        return 0
    else:
        return n


def line(size=42):
    return "-" * size

def header(txt):
    print(line())
    print(txt.center(42))
    print(line())

def menu(lst):
    header("MAIN MENU")
    c = 1
    for item in lst:
        print(f"\033[33m{c}\033[0m - {item}")
        c += 1
    print(line())
    option = readint("\033[33mChoose an option: \033[0m")
    return option