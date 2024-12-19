import os

def list_directory(path):
    """Выводит содержимое указанной директории."""
    try:
        items = os.listdir(path)
        print("\nСодержимое директории:")
        for item in items:
            print(item)
    except FileNotFoundError:
        print("Ошибка: Директория не найдена.")
    except PermissionError:
        print("Ошибка: Доступ запрещен.")

def delete_item(path):
    """Удаляет файл или директорию по указанному пути."""
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"Файл '{path}' успешно удален.")
        elif os.path.isdir(path):
            os.rmdir(path)
            print(f"Директория '{path}' успешно удалена.")
        else:
            print("Ошибка: Указанный путь не является файлом или директорией.")
    except FileNotFoundError:
        print("Ошибка: Файл или директория не найдены.")
    except PermissionError:
        print("Ошибка: Доступ запрещен.")
    except OSError as e:
        print(f"Ошибка: Не удалось удалить '{path}'. {e}")

def rename_item(old_path, new_name):
    """Переименовывает файл или директорию."""
    try:
        new_path = os.path.join(os.path.dirname(old_path), new_name)
        os.rename(old_path, new_path)
        print(f"'{old_path}' переименован в '{new_path}'.")
    except FileNotFoundError:
        print("Ошибка: Файл или директория не найдены.")
    except PermissionError:
        print("Ошибка: Доступ запрещен.")
    except OSError as e:
        print(f"Ошибка: Не удалось переименовать '{old_path}'. {e}")

def main():
    while True:
        print("\nФайловый менеджер:")
        print("1 - Раскрыть директорию")
        print("2 - Удалить файл/папку")
        print("3 - Переименовать файл/папку")
        print("4 - Выйти")

        choice = input("Введите номер операции: ").strip()

        if choice == "1":
            path = input("Введите путь к директории: ").strip()
            list_directory(path)
        elif choice == "2":
            path = input("Введите путь к файлу/папке для удаления: ").strip()
            delete_item(path)
        elif choice == "3":
            old_path = input("Введите старый путь: ").strip()
            new_name = input("Введите новое имя: ").strip()
            rename_item(old_path, new_name)
        elif choice == '4':
            break
        else:
            print("Ошибка: Неизвестная команда.")

if __name__ == "__main__":
    main()

