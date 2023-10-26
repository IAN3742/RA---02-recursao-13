def sequenciaD(p, q, n):
    if n == 1:
        return p
    elif n % 2 == 0:
        return sequenciaD(p, q, n - 1) + q
    else:
        return sequenciaD(p, q, n - 1) - q
