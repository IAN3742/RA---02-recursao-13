def pertence(cadeia):
    if cadeia == 'a' or cadeia == 'b':
        return True
    elif cadeia[-1] == 'b':
        return pertence(cadeia[:-1])
    else:
        return False

cadeias = ['a', 'ab', 'aba', 'aaab', 'bbbbb']
for cadeia in cadeias:
    if pertence(cadeia):
        print(f'"O caracter {cadeia}" pertence a S.')
    else:
        print(f'"O caractér {cadeia}" não pertence a S.')
