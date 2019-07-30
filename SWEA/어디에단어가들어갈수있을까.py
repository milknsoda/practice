testcase = int(input())

for case in range(testcase):
    n, k = map(int, input().split())
    puzzle = []
    for _ in range(n):
        width = [x for x in map(int, input().split())]
        puzzle.append(width)
    
    # 가로줄 검증
    count = 0
    crossword = 0
    for p in puzzle:
        for i in p:
            if i:
                count += 1
            else:
                if count == k:
                    crossword += 1
                count = 0
        if count == k:
            crossword += 1
        count = 0

    # 세로줄 검증
    for r in range(n):
        count = 0
        for c in range(n):
            if puzzle[c][r]:
                count += 1
            else:
                if count == k:
                    crossword += 1
                count = 0
        if count == k:
            crossword += 1

    print(f'#{case+1} {crossword}')