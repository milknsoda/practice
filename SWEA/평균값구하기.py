# 테스트 케이스 개수와 공백문자로 구분된 숫자 10개씩 받아 평균을 구한다.
test_case = int(input())

for i in range(test_case):
    digits = input().split()
    result = 0
    for digit in digits:
        result += int(digit)
    print(f'#{i+1} {result/10}')
    # print(f'#{i+1} {round(result/10)}') # 소수점 첫째 자리에서 반올림