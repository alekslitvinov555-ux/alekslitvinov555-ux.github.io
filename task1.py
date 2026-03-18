# Задача 1: Функція, яка отримує два списки чисел і повертає список
# елементів, які присутні в обох списках.

def spilni_elementy(list1, list2):
    result = []
    for elem in list1:
        if elem in list2 and elem not in result:
            result.append(elem)
    return result


# Тест
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

print("Список 1:", a)
print("Список 2:", b)
print("Спільні елементи:", spilni_elementy(a, b))

a2 = [10, 20, 30, 40]
b2 = [20, 40, 60]

print("\nСписок 1:", a2)
print("Список 2:", b2)
print("Спільні елементи:", spilni_elementy(a2, b2))
