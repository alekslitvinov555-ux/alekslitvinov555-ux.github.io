# Задача 2: Програма, яка рахує кількість парних і непарних чисел
# у списку, введеному користувачем.

vvid = input("Введіть числа через пробіл: ")
chysla = vvid.split()

parni = 0
neparni = 0

for s in chysla:
    n = int(s)
    if n % 2 == 0:
        parni += 1
    else:
        neparni += 1

print("Кількість парних чисел:", parni)
print("Кількість непарних чисел:", neparni)
