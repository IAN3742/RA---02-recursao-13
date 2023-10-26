def sequenciaA(n):
    if n == 1:
        return 1
    else:
        return 3 * sequenciaA(n - 1)
