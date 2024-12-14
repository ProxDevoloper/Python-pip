import colorama

# Инициализация colorama
colorama.init()

# Получаем список всех атрибутов модуля
print("Все атрибуты модуля colorama:\n")
for attribute in dir(colorama):
    print(attribute)

# Фильтруем и выводим только важные атрибуты и классы
print("\nКлассы в модуле colorama:")
for attribute in dir(colorama):
    obj = getattr(colorama, attribute)
    # Проверяем, что это класс
    if isinstance(obj, type):
        print(f"Класс: {attribute}")

print("\nФункции в модуле colorama:")
for attribute in dir(colorama):
    obj = getattr(colorama, attribute)
    # Проверяем, что это функция (callable)
    if callable(obj) and not isinstance(obj, type):
        print(f"Функция: {attribute}")

# Пример работы с одним из классов
print("\nАтрибуты класса Fore:")
for attr in dir(colorama.Fore):
    if not attr.startswith("__"):  # Пропускаем магические методы
        print(f"{attr}: {getattr(colorama.Fore, attr)}")
