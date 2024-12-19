import pickle

# Создание словаря с магазинами и их выручкой
stores = {
    'Магазин A': {'Понедельник': 1000, 'Вторник': 1200, 'Среда': 1100, 'Четверг': 1300, 'Пятница': 1500, 'Суббота': 1400, 'Воскресенье': 1600},
    'Магазин B': {'Понедельник': 800, 'Вторник': 900, 'Среда': 950, 'Четверг': 1000, 'Пятница': 1100, 'Суббота': 1200, 'Воскресенье': 1300},
    'Магазин C': {'Понедельник': 700, 'Вторник': 800, 'Среда': 750, 'Четверг': 800, 'Пятница': 900, 'Суббота': 950, 'Воскресенье': 1000},
    'Магазин D': {'Понедельник': 1500, 'Вторник': 1600, 'Среда': 1550, 'Четверг': 1700, 'Пятница': 1800, 'Суббота': 1900, 'Воскресенье': 2000},
    'Магазин E': {'Понедельник': 600, 'Вторник': 700, 'Среда': 650, 'Четверг': 600, 'Пятница': 750, 'Суббота': 800, 'Воскресенье': 850},
    'Магазин F': {'Понедельник': 1200, 'Вторник': 1300, 'Среда': 1250, 'Четверг': 1400, 'Пятница': 1500, 'Суббота': 1600, 'Воскресенье': 1700},
    'Магазин G': {'Понедельник': 900, 'Вторник': 950, 'Среда': 1000, 'Четверг': 1050, 'Пятница': 1100, 'Суббота': 1150, 'Воскресенье': 1200}
}

# Вычисление средней выручки для каждого магазина
average_revenue = {}
for store, revenues in stores.items():
    avg = sum(revenues.values()) / len(revenues)
    average_revenue[store] = avg

# Вывод списка магазинов и их средней выручки
print("Средняя выручка магазинов:")
for store, avg in average_revenue.items():
    print(f"{store}: {avg:.2f}")

# Находим магазин с максимальной и минимальной средней выручкой
max_store = max(average_revenue, key=average_revenue.get)
min_store = min(average_revenue, key=average_revenue.get)

print(f"\nМагазин с максимальной средней выручкой: {max_store} ({average_revenue[max_store]:.2f})")
print(f"Магазин с минимальной средней выручкой: {min_store} ({average_revenue[min_store]:.2f})")

# Неблагоприятный день для каждого магазина
unfavorable_days = {}
for store, revenues in stores.items():
    min_day = min(revenues, key=revenues.get)
    unfavorable_days[store] = min_day

print("\nНаиболее неблагоприятные дни для работы:")
for store, day in unfavorable_days.items():
    print(f"{store}: {day}")

# Магазины с выручкой в воскресенье более чем на 20% выше средней
stores_above_average = {}
for store in stores:
    if stores[store]['Воскресенье'] > average_revenue[store] * 1.2:
        stores_above_average[store] = stores[store]

print("\nМагазины с выручкой в воскресенье выше средней более чем на 20%:")
for store in stores_above_average:
    print(store)

# Сохранение словаря в бинарный файл
with open('data.pickle', 'wb') as f:
    pickle.dump(stores, f)

# Чтение данных из бинарного файла
with open('data.pickle', 'rb') as f:
    loaded_stores = pickle.load(f)

print("\nДанные из бинарного файла:")
print(loaded_stores)
