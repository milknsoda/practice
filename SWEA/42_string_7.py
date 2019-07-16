# 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램

# 1. 문자열을 입력받는다.
string = input()

for i in range(len(string)):
    if not i % 2:
        print(string[i], end='')
