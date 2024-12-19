import json

def read_json(file_path):
    """Чтение JSON файла и преобразование в словарь."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def filter_users_by_id(data, id_prefix):
    """Фильтрация пользователей по первым трём символам идентификатора."""
    return [user for user in data if user["id"].startswith(id_prefix)]

def write_json(file_path, data):
    """Запись данных в JSON файл."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Чтение и фильтрация JSON
json_file = "lab.json"
json_data = read_json(json_file)

# Фильтрация по первым трём символам идентификатора
filtered_data = filter_users_by_id(json_data, "ABC")

# Запись отфильтрованных данных в out.json
output_file = "out.json"
write_json(output_file, filtered_data)

print(f"Отфильтрованные данные записаны в {output_file}.")
