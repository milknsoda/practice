test_case = int(input())

distance = 0
speed = 0
for i in range(test_case):
    n = int(input())
    for _ in range(n):
        n1, s1 = input().split()
        if n1 == 0:
            continue
        elif n1 == 1:
            speed += int(s1)
        elif n1 == 2:
            speed -= int(s1)
            if speed <= 0:
                speed = 0
        distance += speed
    print(f'#{i+1} {distance}')