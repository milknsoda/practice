def my_sqrt(n):
    for i in range(1, n):
        if i**2 <= n < (i+1)**2:
            l = i
            r = i + 1
    if n <= 0:
        return '잘못된 입력'
    elif n == 1:
        return 1
    while abs(l**2 - n) >= 1e-10:
        if n < ((r + l) / 2)**2:
            r = (r + l) / 2
        elif n > ((r + l) / 2)**2:
            l = (r + l) / 2
        print(l, r)
    print(l)
