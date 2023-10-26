
def B(n):
    if n == 1:
        return 1
    else:
        return B(n - 1) + n ** 2

n = 5 
resultado = B(n)
print(f'B({n}) = {resultado}')
