# 문장을 구성하는 단어를 역순으로 출력하는 프로그램
# 1. 문장을 입력받는다.
sts = input()

# 2. 문장을 단어 단위로 구분한다.
sts_list = sts.split(' ')
print(sts_list)

# 3. 구분한 단어를 역순으로 배치한다.
sts_list.reverse()
print(sts_list)

# 4. 역순으로 배치한 단어를 문장으로 출력한다.
result = ''
for i in sts_list:
    result = f'{result} {i}'
print(result.strip())