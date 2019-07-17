# 1. test case 수를 입력받는다.
test_case = int(input())
# 2. 각 테스트 케이스가 공백문자로 구분되어 입력된다.
for i in range(test_case):
    nums = map(int, input().split())
    print(f'#{i+1} {max(nums)}')