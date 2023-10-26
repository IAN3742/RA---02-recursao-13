def pertence(numero):
    if numero == 2 or numero == 3:
        return True
    elif numero % 2 == 0:
        return pertence(numero // 2)
    elif numero % 3 == 0:
        return pertence(numero // 3)
    else:
        return False

numeros = [6, 9, 16, 21, 26, 54, 72, 218]

for n in numeros:
    if pertence(n):
        print(f"O número {n} pertence a M.")
    else:
        print(f"O número {n} não pertence a M.")

