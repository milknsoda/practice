testcase = int(input())

for case in range(testcase):    
    sdoku = [input().split() for _ in range(9)]
    result = True

    # 가로 검증
    for width in sdoku:
        if len(set(width)) != 9:
            result = False
    # 세로 검증
    for height in range(9):
        verify = set()
        for width in range(9):
            verify.update(sdoku[width][height])
        if len(verify) != 9:
            result = False
    # 구획 검증
    for num in range(0,7,3):
        section = set()
        for height in range(3):
            for width in range(3):
                section.update(sdoku[height+num][width+num])
        if len(section) != 9:
            result = False
    # 결과 출력
    print(f'#{case+1} ', end='')
    if result:
        print(1)
    else:
        print(0)
