n, m = map(int, input().split())
arrangement = []
total = 0
for i in range(n):
    line = list(map(int, input().split()))
    arrangement.append(line)
print(arrangement)
result = 0
for row in range(n):
    for column in range(n):
        total = 0
        for swatter in range(m):
            if row + (m-1) < n and column + (m-1) < n:
                total += arrangement[row+swatter][column+swatter]
        if result < total:
            result = total
print(result)