# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.


# [제약 사항]

# 각 수는 0 이상 10000 이하의 정수이다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.


# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

tc = int(input('테스트 케이스 수: '))
nums = []

for i in range(tc):
    num = input().split()
    num = list(map(int, num))
    nums.append(num)

print(num)
print(nums)

for i in range(tc):
    result = 0
    for k in nums[i]:
        if k % 2:
            result += k
    print(f'#{i+1} {result}')

# for k in range(tc):
#     result = sum(nums[k])
#     print(f'#{k+1}', end=' ')
#     print(result)
