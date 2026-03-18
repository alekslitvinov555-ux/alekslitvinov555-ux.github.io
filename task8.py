# Задача 8: Функція, яка отримує два рядки і повертає True,
# якщо вони містять однаковий набір букв (ігноруючи регістр).

def odnakovyi_nabir(s1, s2):
    s1_lower = s1.lower()
    s2_lower = s2.lower()

    bukvy1 = []
    for b in s1_lower:
        if b.isalpha() and b not in bukvy1:
            bukvy1.append(b)

    bukvy2 = []
    for b in s2_lower:
        if b.isalpha() and b not in bukvy2:
            bukvy2.append(b)

    bukvy1.sort()
    bukvy2.sort()

    return bukvy1 == bukvy2


# Тест
print("'listen' і 'silent':", odnakovyi_nabir("listen", "silent"))
print("'hello' і 'world':", odnakovyi_nabir("hello", "world"))
print("'ABC' і 'cab':", odnakovyi_nabir("ABC", "cab"))
print("'Python' і 'typhon':", odnakovyi_nabir("Python", "typhon"))
print("'abc' і 'abcd':", odnakovyi_nabir("abc", "abcd"))
