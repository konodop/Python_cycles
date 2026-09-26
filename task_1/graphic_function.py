start, end, dx = map(float, input().split())

x = start

while -7 <= x <= -3:
    y = 3
    print(x, "|", y)
    x += dx
while -3 < x <= 3:
    y = -((9 - x ** 2) ** 0.5) + 3
    print(x, "|", y)
    x += dx
while 3 < x <= 6:
    y = -2 * x + 9
    print(x, "|", y)
    x += dx
while 6 < x <= 11:
    y = x - 9
    print(x, "|", y)
    x += dx