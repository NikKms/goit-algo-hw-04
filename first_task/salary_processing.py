def total_salary(path):
    salary = list()

    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    parts = line.split(",")
                    if len(parts) > 1:
                        salary.append(float(parts[1]))
                except (ValueError, IndexError):
                    continue

        if not salary:
            return "NO VALID SALARY DATA"

        return (sum(salary), sum(salary) / len(salary))

    except FileNotFoundError:
        return "FILE NOT FOUND"
    except (OSError, IOError):
        return "CANT READ FILE"


def process_salary_data(result):
    if  len(result) == 2:
        total, average = result
        return f"Загальна сума заробітної плати: {total},\nСередня заробітна плата: {average}"
    else:
        return result