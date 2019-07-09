# 입력받은 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 코드

string = input()
letter = 0
integer = 0
for char in string:
    if char is ' ':
        continue
    try:
        int(char)
        integer = integer + 1
    except:
        if ord('a') <= ord(char) <= ord('Z') or ord('ㄱ') <= ord(char) <= ord('힣'):
            letter = letter + 1
print(f'LETTERS {letter}')
print(f'DIGITS {integer}')