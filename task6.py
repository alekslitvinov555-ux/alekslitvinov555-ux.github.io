# Задача 6: Програма, яка отримує список слів і повертає новий список,
# де кожне слово написане задом наперед.

def slova_navpaky(lst):
    result = []
    for slovo in lst:
        result.append(slovo[::-1])
    return result


# Тест
slova1 = ["привіт", "світ", "python"]
print("Вхідний список:", slova1)
print("Результат:", slova_navpaky(slova1))

slova2 = ["abcd", "hello", "level", "radar"]
print("\nВхідний список:", slova2)
print("Результат:", slova_navpaky(slova2))
