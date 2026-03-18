# Задача 3: Функція, яка отримує рядок і повертає його у вигляді
# списку слів у верхньому регістрі.

def slova_u_verkh(ryadok):
    slova = ryadok.split()
    result = []
    for slovo in slova:
        result.append(slovo.upper())
    return result


# Тест
test1 = "привіт як справи"
print("Рядок:", test1)
print("Результат:", slova_u_verkh(test1))

test2 = "hello world python programming"
print("\nРядок:", test2)
print("Результат:", slova_u_verkh(test2))
