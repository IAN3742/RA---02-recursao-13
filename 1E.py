
def D(n):
    if n == 1:
        return 3
    elif n == 2:
        return 5
    else:
        return (n - 1) * D(n - 1) + (n - 2) * D(n - 2)

n = 5 
resultado = D(n)
print(f'D({n}) = {resultado}')

