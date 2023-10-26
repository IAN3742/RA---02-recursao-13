def S(n):
    if n == 1:
        return 10
    else:
        return S(n - 1) + 10


n = 5
resultado = S(n)
print(f"O valor de S({n}) é {resultado}.")
