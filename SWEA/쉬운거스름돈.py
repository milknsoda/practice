testcase = int(input())

for case in range(testcase):    
    money = [0] * 8

    sum_money = int(input())

    m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for idx, n in enumerate(m):
        if sum_money // n:
            money[idx] = sum_money // n
            sum_money = sum_money % n

    result = ''
    for i in money:
        result += str(i) + ' '
    print(f'#{case+1}')
    print(result)