def sequenciaC(a, b, n):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return sequenciaC(a, b, n - 1) + n * sequenciaC(a, b, n - 2)
