# Задача 4: Програма, яка генерує список із 50 випадкових чисел та
# знаходить середнє значення всіх парних чисел. Порівнює це значення з
# номером по списку (позиція курсанта у списку групи).
# Якщо середнє більше – виводить це значення. Інакше – генерує список знову.

import random

NOMER_PO_SPYSKU = 15  # номер курсанта у списку групи

while True:
    chysla = []
    for i in range(50):
        chysla.append(random.randint(1, 100))

    parni = []
    for n in chysla:
        if n % 2 == 0:
            parni.append(n)

    if len(parni) == 0:
        continue

    seredne = sum(parni) / len(parni)

    print("Список:", chysla)
    print("Парні числа:", parni)
    print(f"Середнє парних: {seredne:.2f}")
    print(f"Номер по списку: {NOMER_PO_SPYSKU}")

    if seredne > NOMER_PO_SPYSKU:
        print(f"Середнє значення парних ({seredne:.2f}) більше за номер по списку ({NOMER_PO_SPYSKU})")
        break
    else:
        print("Середнє менше або рівне номеру по списку. Генеруємо список знову...\n")
