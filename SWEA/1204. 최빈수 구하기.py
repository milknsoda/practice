test_case = int(input())

for i in range(test_case):
    test_num = int(input())
    # 입력받은 숫자를 공백을 기준을 나눠 리스트로 만든다.
    scores = map(int, input().split())
    # 리스트를 셋으로 형변환하여 중복된 항목을 제거하고,
    score_set = set(scores)
    # 빈 딕셔너리를 만든 후, 셋의 각 항목을 키로 하고 값을 0으로 하는 딕셔너리를 만든다.
    score_dic = {}
    for a in score_set:
        if a in score_dic:
            score_dic[a] += 1
        else:
            score_dic[a] = 1
    
    
    # 빈 딕셔너리의 키와 비교하여 각 값의 개수를 체크한다.
