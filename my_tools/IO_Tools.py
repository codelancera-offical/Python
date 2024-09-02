import time
import sys
from colorama import Fore, Style, init


def print_slowly(text=None, color="white", delay=0.05):
    init(autoreset=False)


    # Define a dictionary to map simple color names to colorama codes
    color_map = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "reset": Style.RESET_ALL
    }

    color_code = color_map.get(color.lower(), Fore.WHITE)   # default is white
    sys.stdout.write(color_code)
    sys.stdout.flush()

    if text is None:
        text = input("Please input some text: ")

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(Style.RESET_ALL)
    sys.stdout.flush()


    sys.stdout.write("\n")
    return True

def main():
    functions = {
        "0": print_slowly
    }

    print("All IO tools example: ")
    for key, value in functions.items():
        print(f"\t{key}: {value.__name__}") # print name of function

    choice = input("Choose a net operation: ")

    if choice in functions:
        result = functions[choice]()
        if result is not None:
            print(result)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
