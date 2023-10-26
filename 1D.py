def P(n):
    if n == 1:
        return 1
    else:
        return n * n * P(n - 1) + n - 1

resultado = P(5)

print(resultado)

