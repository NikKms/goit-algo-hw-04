from cat_utils import get_cats_info

file_path = "../data/cats.txt"

def main():
    path = file_path
    cats_info = get_cats_info(path)
    print(cats_info)

if __name__ == "__main__":
    main()
