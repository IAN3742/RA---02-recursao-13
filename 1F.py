
def W(n):
    if n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        return W(n - 1) * W(n - 2)

n = 5 
resultado = W(n)
print(f'W({n}) = {resultado}')
