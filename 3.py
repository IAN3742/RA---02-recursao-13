def pertence_T(numero):
    if numero == 2:
        return True
    if numero < 2:
        return False
    if numero % 2 == 0:
        return pertence_T(numero // 2)
    if numero % 2 == 1:
        return pertence_T(numero - 3)
    return False

numeros = [6, 7, 19, 12]

for numero in numeros:
    if pertence_T(numero):
        print(f"{numero} pertence a T")
    else:
        print(f"{numero} não pertence a T")
