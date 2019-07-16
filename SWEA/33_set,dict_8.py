string = input()
upper = 0
lower = 0
for letter in string:
    if 'a' <= letter <= 'z':
        lower = lower + 1
    elif 'A' <= letter <= 'Z':
        upper = upper + 1
print(f'UPPER CASE {upper}')
print(f'LOWER CASE {lower}')