def f(x, y):
    return (2 * abs(x) - y) / (y ** 2)

x, y = map(int, input().split())

if x > 0:
    if y < 0:
        print('Точка принадлежит 4 четверти')
        if abs(x) > abs(y):
            print('Координата х - наибольшая по модулю')
        elif abs(x) < abs(y):
            print('Координата у - наибольшая по модулю')
        else:
            print('Координаты равны по модулю')
    else:
        print('Точка принадлежит 1 четверти')
        print('Введите две строки:')
        s1 = str(input())
        s2 = str(input())
        if len(s1) < len(s2):
            print(s1)
        else:
            print(s2)
else:
    if y < 0:
        print('Точка принадлежит 3 четверти')
        print('Введите строку')
        s1 = int(input())
        print(x * len(s1), y * len(s1))
    else:
        print('Точка принадлежит 2 четверти')
        print(f(x, y))