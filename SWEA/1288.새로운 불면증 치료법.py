test_case = int(input())

# 테스트 케이스만큼 반복
for i in range(test_case):
    # 숫자를 입력받고,
    n_num = int(input())
    n_value = n_num
    num_set = set()
    count = 1
    # 반복하면서 c_set과 num_set이 같아지면 종료
    while len(num_set) != 10:
        # 각 자릿수의 숫자들을 각각 모은다.
        for k in str(n_value):
            num_set.update(k)
        # count에 1을 더하고 입력받은 숫자에 다시 곱한다.
        count += 1
        n_value = n_num * count
        print(n_value)
    # 모아진 숫자들이 0~9까지 모두 존재하면 n_num * (count-1) 출력하고 종료
    print(f'#{i+1} {n_num*(count-1)}')

