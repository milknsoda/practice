# 테스트 케이스 개수와 공백으로 구분된 숫자 2개의 숫자를 입력받아 대,소 비교 후 등호,부등호 출력
test_case = int(input())

for i in range(test_case):
    compare = input().split()
    compare = list(map(int, compare))
    if compare[0] > compare[1]:
        print(f'#{i+1} >')
    elif compare[0] < compare[1]:
        print(f'#{i+1} <')
    else:
        print(f'#{i+1} =')