test_case = int(input())

for case in range(test_case):
    n = int(input())
    count = [0] * 51
    nums = list(map(int, input().split()))
    for i in nums:
        count[i] += 1
    for j in range(1, 51):
        count[j] += count[j - 1]
    result = [0] * n
    for k in range(n-1, -1, -1):
        result[count[nums[k]]-1] = nums[k]
        count[nums[k]] -= 1
    sort_list = ''
    for a in result:
        sort_list += str(a)
        if a != result[-1]:
            sort_list += ' '
    print('#{} {}'.format(case+1, sort_list))

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    result = ''
    for a in nums:
        result += str(a) + ' '
    print()