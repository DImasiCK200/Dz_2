n = int(input())
x = n
a = []

while n > 0:
    a.append(n % 10)
    n //= 10
a = a[::-1]

if max(a) - min(a) == a[1]:
    print('Число ', x, ' - "интересное"')
else:
    print('Число ', x, ' - не "интересное"')