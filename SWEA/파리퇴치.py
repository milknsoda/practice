testcase = int(input())

for case in range(testcase)
    # N x N 의 배열을 만든다.
    n, m = map(int, input().split())
    arrangement = []
    total = 0
    for i in range(n):
        line = list(map(int, input().split()))
        arrangement.append(line)
    # M x M 의 파리채안의 파리 수의 합 중에서 가장 큰 수를 출력한다.
    result = 0
    for row in range(n):
        for column in range(n):
            total = 0
            for swatter in range(m):
                if row + (m-1) < n and column + (m-1) < n:
                    total += arrangement[row+swatter][column+swatter]
                    if swatter != 0:
                        total += arrangement[row][column + swatter]
                        total += arrangement[row+swatter][column]
            if result < total:
                result = total
    print(f'#{case+1} {result}')