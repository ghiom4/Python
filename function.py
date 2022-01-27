
def somme(*args):
    total = 0
    for i in args:
        try:
            total += i
        except TypeError:
            next
    return total

print(somme(1, 2))
print(somme(10, 4, 12))
print(somme(2, 2, "b"))