base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
base64_en = dict(enumerate(base64))

# 0. 6비트의 2진수로 변환하는 함수
def detobi(x):
    num = x
    debi = ''
    while num//2 != 0:
        debi += str(num % 2)
        num = num // 2
    if num == 1:
        debi += '1'
    debi = debi[::-1]
    return '{0:0>6}'.format(debi)
# 0. 2진수를 10진수로 변환하는 함수
def bitode(y):
    num = y[::-1]
    result = 0
    for key, bi in dict(enumerate(num)).items():
        if int(bi) == 1:
            result += 2**key
    return result

# 1. 테스트 케이스 수를 입력받는다.
test_case = int(input())
# 2. 테스트 케이스 수만큼 반복
for i in range(test_case):
    # 3. 각 테스트 케이스를 입력받고, for문을 통해 한글자씩 읽는다.
    b64s = input()
    decode = []
    for text in b64s:
        # 4. 읽은 문자와 base64_en의 값을 비교하여 키값을 비어있는 decode리스트에 추가한다.
        for key, char in base64_en.items():
            if text == char:
                decode.append(key)
    # 5. 비어있는 스트링 decode_bi를 선언하고, decode의 값들을 2진수로 변환하여 decode_bi에 순서대로 추가한다.
    decode_bi = ''
    for num in decode:
        decode_bi += detobi(num)
    # 6. 2진수의 문자열을 8자리씩 끊어서 리스트로 만든다.
    new_dcode = []
    for k in range(0, len(decode_bi), 8):
        new_dcode.append(decode_bi[k:k+8])
    print(new_dcode)
    # 7. 비어있는 스트링을 선언하고, 리스트의 각 2진수를 10진수로 변환하고,
    new_string = ''
    for end in new_dcode:
        # 8. 비어있는 스트링에 10진수를 해당하는 아스키 문자로 변환하여 추가한다.
        new_string += chr(bitode(end))
    print(f'#{i+1} {new_string}')