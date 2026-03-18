# Задача 7: Програма, яка обчислює суму всіх чисел у рядку,
# де числа відокремлені пробілами.

def suma_chysel(ryadok):
    chastyny = ryadok.split()
    suma = 0
    for ch in chastyny:
        suma += int(ch)
    return suma


# Тест
r1 = "1 2 3 4 5"
print(f"Рядок: '{r1}'")
print("Сума:", suma_chysel(r1))

r2 = "10 20 30 40 50"
print(f"\nРядок: '{r2}'")
print("Сума:", suma_chysel(r2))

r3 = "7 14 3 100"
print(f"\nРядок: '{r3}'")
print("Сума:", suma_chysel(r3))
