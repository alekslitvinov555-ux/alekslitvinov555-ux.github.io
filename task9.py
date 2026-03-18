# Задача 9: Програма, яка генерує випадковий пароль заданої довжини,
# що містить великі та маленькі літери, цифри та спеціальні символи.

import random

def zgeneruvaty_parol(dovzhyna):
    velyki = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mali = "abcdefghijklmnopqrstuvwxyz"
    cyfry = "0123456789"
    spetsialni = "!@#$%^&*()-_=+[]{}|;:,.<>?"

    vsi_symvoly = velyki + mali + cyfry + spetsialni

    # Гарантуємо наявність кожного типу символів
    parol = []
    parol.append(random.choice(velyki))
    parol.append(random.choice(mali))
    parol.append(random.choice(cyfry))
    parol.append(random.choice(spetsialni))

    for i in range(dovzhyna - 4):
        parol.append(random.choice(vsi_symvoly))

    random.shuffle(parol)
    return "".join(parol)


dovzhyna = int(input("Введіть довжину пароля (мінімум 4): "))

if dovzhyna < 4:
    print("Довжина пароля має бути не менше 4 символів!")
else:
    parol = zgeneruvaty_parol(dovzhyna)
    print("Згенерований пароль:", parol)
