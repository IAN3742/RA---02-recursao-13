def pertence(cadeia):
    if cadeia == 'a' or cadeia == 'b' or cadeia == 'c':
        return True
    elif cadeia[0] == 'a' and cadeia[-1] == 'c' and pertence(cadeia[1:-1]):
        return True
    else:
        return False

cadeias = ['a(b)c', 'a(a(b)c)c', 'a(abc)c', 'a(a(a(a)c)c)c', 'a(aacc)c']
for cadeia in cadeias:
    if pertence(cadeia):
        print(f'"Esses símbolos {cadeia}" pertencem a W.')
    else:
        print(f'"Esses símbolos {cadeia}" não pertencem a W.')
