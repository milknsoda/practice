# 여러 문장을 입력받아 대문자로 변환해 출력하는 프로그램

# 1. 문자열을 입력받는다.
# sts = input()

# 2. 문자열을 대문자로 변환한다.
# sts = sts.upper()
# print(sts)

# 3. 이것을 무한반복하고, 공백으로 남겨둘 경우 종료시킨다.

while True:
    sts = input()
    if sts == '':
        break
    sts = sts.upper()
    print(f'>> {sts}')