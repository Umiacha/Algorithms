def find_NOD_Euclid(a: int, b: int) -> int:
    """Алгоритм поиска Н.О.Д. двух чисел по алгоритму Евклида.
    
    Идея в том, что для a < b: НОД(a, b) = НОД(b, a % b).
    """
    if a == b:  # corner case
        return a
    elif a < b:
        a, b = b, a
    mod = a % b
    if mod == 0:
        return b
    else:
        return find_NOD_Euclid(b, mod)


if __name__ == '__main__':
    a, b = map(int, input('Введите два целых числа (больше нуля) через пробел: ').split())
    print(f'Их НОД = {find_NOD_Euclid(a, b)}')