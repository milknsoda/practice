# 25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다.
# 다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.
# 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
# 1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
# 2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
# 3. 판매는 얼마든지 할 수 있다.
# 예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.

# 1. text case 개수를 입력받는다.
test_case = int(input())

for i in range(test_case):
    # 2. 테스트 케이스만큼 반복하면서, 각 테스트 케이스마다 N을 입력받는다.
    n_days = int(input())
    # 3. N일동안의 가격을 공백문자를 기준으로 나눠 입력받는다.
    n_values = list(map(int,input().split()))
    en_v = list(enumerate(n_values))
    print(en_v[0][1])

    # 4. n_days 범위만큼 반복하여 각 인덱스의 값이 그 뒤의 나머지 값들과 비교하여 사고 팔 것을 결정한다.
    # result_a = 0
    # for k in range(n_days):
    #     result = 0
    #     for key, value in enumerate(n_values):
    #         if key > k and n_values[k] < value:
    #             if result < value - n_values[k]:
    #                 result = value - n_values[k]
    #     result_a += result
    # print(f'#{i+1} {result_a}')