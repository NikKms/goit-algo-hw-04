import sys
from pathlib import Path
from colorama import Fore, Style

def print_dir_structure(path: Path, tab=0):
    if not path.is_dir():
        print(Fore.RED + "Шлях не веде до директорії або такої директорії не існує")
        return

    for item in path.iterdir():
        tabs = " " * (tab * 2)
        if item.is_dir():
            print(f"{tabs}📂 {Fore.BLUE}{item.name}")

            print_dir_structure(item, tab+1)
        else:
            print(f"{tabs}📜 {Fore.GREEN}{item.name}")


def main():
    if len(sys.argv) < 2 :
        print(Fore.RED + "Введіть шлях до директорії!")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + f"{dir_path} не існує")
        sys.exit(1)

    print_dir_structure(dir_path)

if __name__ == "__main__":
    main()