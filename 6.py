result = []

def divider(a, b):
    if a < b:
        raise ValueError("Первый аргумент меньше второго")
    if b > 100:
        raise IndexError("Второй аргумент больше 100")
    return a / b

data = {
    10: 2,
    2: 5,
    "123": 4,
    18: 0,
    8: 4
} 

for key in data:
    try:
        res = divider(int(key), data[key])
        result.append(res)
    except ZeroDivisionError:
        print(f"Ошибка: Деление на ноль при обработке пары ({key}, {data[key]})")
    except TypeError:
        print(f"Ошибка: Некорректный тип данных для пары ({key}, {data[key]})")
    except ValueError as e:
        print(f"Ошибка: {e} для пары ({key}, {data[key]})")
    except IndexError as e:
        print(f"Ошибка: {e} для пары ({key}, {data[key]})")

print("Результат:", result)
