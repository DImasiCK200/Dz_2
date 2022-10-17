S = float(input())
t = float(input())

v = S / t

if v < 30:
    print('Медленно')
elif v >= 30 and v <= 60:
    print('Средне')
else:
    print('Быстро')