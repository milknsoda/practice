testcase = int(input())

for case in range(testcase):
    hour1, min1, hour2, min2 = map(int, input().split())
    tm_h = 0

    if min1 + min2 >= 60:
        tm_m = min1 + min2 - 60
        tm_h += 1
    else:
        tm_m = min1 + min2

    if hour1 + hour2 + tm_h > 12:
        tm_h = hour1 + hour2 + tm_h - 12
    else:
        tm_h = hour1 + hour2 + tm_h

    print(f'#{case+1} {tm_h} {tm_m}')