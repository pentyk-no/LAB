import csv

# Чтение содержимого CSV файла
def read_csv(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
import csv

# Чтение содержимого CSV файла
def read_csv(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            formatted_row = {key.strip(): value.strip() for key, value in row.items()}
            data.append(formatted_row)
    return data

# Вывод содержимого в формате "Ключ → Значение"
def display_data(data):
    for i, row in enumerate(data, start=1):
        print(f"Строка {i}:")
        for key, value in row.items():
            print(f"  {key} → {value}")
        print()

# Получение минимального значения по столбцу
def get_min(data, column):
    return min(float(row[column]) for row in data)

# Получение максимального значения по столбцу
def get_max(data, column):
    return max(float(row[column]) for row in data)

# Сумма значений по столбцу
def get_sum(data, column):
    return sum(float(row[column]) for row in data)

# Количество строк с непустым значением в столбце
def get_count(data, column):
    return sum(1 for row in data if row[column])

# Среднее значение по столбцу
def get_average(data, column):
    return get_sum(data, column) / get_count(data, column)


if __name__ == "__main__":
    file_name = "7.csv"
    data = read_csv(file_name)

    print("Содержимое файла:")
    display_data(data)

    # Пример использования функций
    column = "Sell"

    print(f"Минимальное значение в столбце '{column}': {get_min(data, column)}")
    print(f"Максимальное значение в столбце '{column}': {get_max(data, column)}")
    print(f"Сумма значений в столбце '{column}': {get_sum(data, column)}")
    print(f"Количество строк в столбце '{column}': {get_count(data, column)}")
    print(f"Среднее значение в столбце '{column}': {get_average(data, column)}")
