# A definição recursiva para A(n), número de bactérias presentes no
# início do n-ésimo período de tempo pode ser dada por:

# A(0)=50000
# A(n)=3×A(n−1)

def A(n):
    if n == 0:
        return 50000
    else:
        return 3 * A(n - 1)

população = 50000
quantidade_leituras = 0
while população <= 200000:
    população = A(quantidade_leituras)
    quantidade_leituras += 1

print(f"A população excede 200.000 bactérias após {quantidade_leituras} leituras.")
