def triangular(n):
    if n == 1:
        return 1
    else:
        return n + triangular(n - 1)

n = int(input("Digite o valor de n: "))
resultado = triangular(n)
print(f"O {n}-ésimo número triangular é {resultado}")
