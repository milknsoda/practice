test_case = int(input())

for i in range(test_case):
    P, Q, R, S, W = map(int, input().split())
    if W > R:
        b_bill = Q + (W - R) * S
    else:
        b_bill = Q
    a_bill = P * W
    if a_bill < b_bill:
        print(f'#{i+1} {a_bill}')
    else:
        print(f'#{i+1} {b_bill}')