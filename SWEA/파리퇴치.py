testcase = int(input())

for case in range(testcase):
    # N x N 의 배열을 만든다.
    n, m = map(int, input().split())
    arrangement = []
    total = 0
    for i in range(n):
        line = list(map(int, input().split()))
        arrangement.append(line)
    # M x M 의 파리채 범위 안의 파리 수의 합 중에서 가장 큰 수를 출력한다.
    result = 0
    for row in range(n):
        for column in range(n):
            total = 0
            if row + (m-1) < n and column + (m-1) < n:
                for swat_r in range(m):
                    for swat_c in range(m):
                        total += arrangement[row+swat_r][column+swat_c]
            if result < total:
                result = total
    print(f'#{case+1} {result}')