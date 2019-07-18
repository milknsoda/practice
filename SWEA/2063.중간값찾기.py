# 1. N을 입력받는다.
N_num = int(input())
# 2. N개의 숫자들을 정렬하고 가운데 위치한 숫자를 출력한다.
nums = list(map(int, input().split()))
mid = int(sum(nums)/len(nums))
result = 0
count = 200
for num in nums:
    if abs(num - mid) < count:
        result = num
        count = abs(num - mid)
print(result)