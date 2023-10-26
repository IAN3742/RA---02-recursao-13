
def A(n):
    if n == 1:
        return 2
    else:
        return 1 / A(n - 1)

n = 5  
resultado = A(n)
print(f'A({n}) = {resultado}')
