test_case = int(input())

for i in range(test_case):
    test_num = int(input())
    # 입력받은 숫자를 공백을 기준을 나눠 리스트로 만든다.
    scores = map(int, input().split())
    # 점수가 '0이상 100이하' 이므로 0부터 100까지의 키를 가지고 값으로 0을 가지는 딕셔너리를 만든다.
    score_dict = {}
    for k in range(101):
        score_dict[k] = 0
    # 만든 딕셔너리에 키를 이용하여 점수의 개수를 센다.
    for a in scores:
        score_dict[a] += 1
    # 키와 값을 저장할 변수를 만들고,
    result = 0
    count = 0
    # 딕셔너리의 키와 값을 비교하여 값이 가장 크고, 값이 같을 경우에는 키가 큰 것을 저장한다.
    for key, value in score_dict.items():
        if value > count:
            result = key
            count = value
        elif value == count:
            if key > result:
                result = key
    print(f'{i+1} {result}')

