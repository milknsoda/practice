words = input()
result = []
for i in words:
    result.append(ord(i)-64)
print(' '.join(map(str,result)))
