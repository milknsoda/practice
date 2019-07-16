# 숫자 N을 입력받아서 1~N까지의 정수를 키로 하고, 그 정수의 제곱을 값으로 하는 딕셔너리 객체를 만드는 코드를 작성하시오.
# 1. N을 입력받아 1~N까지의 정수의 리스트를 만든다.
num = range(1, int(input()) + 1) # 입력받은 숫자 + 1을 해야 입력받은 숫자까지의 범위가 생성
# 2. 각 원소를 키로 하고, 그 제곱값을 값으로 하는 딕셔너리를 만든다.
numbers = {}
for s in num:
    numbers[s] = s**2
print(numbers)