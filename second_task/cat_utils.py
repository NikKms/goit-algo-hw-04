def get_cats_info(path):
    cats = list()
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats.append({"id": cat_id, "name": name, "age": age})
        return cats
    except FileNotFoundError:
        return "FILE NOT FOUND"
    except (OSError, IOError):
        return "CANT READ FILE"