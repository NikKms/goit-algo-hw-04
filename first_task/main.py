from salary_processing import total_salary, process_salary_data

file_path = "../data/salary.txt"

def main():
    result = total_salary(file_path)
    formatted_output = process_salary_data(result)
    print(formatted_output)

if __name__ == "__main__":
    main()
