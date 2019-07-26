# 1부터 N*N까지 N x N 의 사각형을 시계방향으로 돌며 채운다

n = int(input())
rectan = [[0 for width in range(n)] for height in range(n)]
count = 1
for ct in range(n):
    if n > 0:
        for width in range(n):
            rectan[0+ct][width+ct] = count
            count += 1
        for height in range(n-1):
            rectan[height+1+ct][n-1+ct] = count
            count += 1
        for width in range(n-1):
            rectan[n-1+ct][-width-2-ct] = count
            count += 1
        for height in range(n-2):
            rectan[-height-2-ct][0+ct] = count
            count += 1
    n -= 2

for i in rectan:
    result = ''
    for k in i:
        result += str(k)
        if k != i[-1]:
            result += ' '
    print(result)

