# Задача 5: Програма, яка перевіряє, чи всі елементи списку унікальні.

def vsi_unikalny(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True


# Тест
lst1 = [1, 2, 3, 4, 5]
print("Список:", lst1)
print("Всі унікальні:", vsi_unikalny(lst1))

lst2 = [1, 2, 3, 2, 5]
print("\nСписок:", lst2)
print("Всі унікальні:", vsi_unikalny(lst2))

lst3 = ["яблуко", "груша", "банан"]
print("\nСписок:", lst3)
print("Всі унікальні:", vsi_unikalny(lst3))

lst4 = ["яблуко", "груша", "яблуко"]
print("\nСписок:", lst4)
print("Всі унікальні:", vsi_unikalny(lst4))
