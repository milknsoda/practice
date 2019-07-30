a = [0, 1, 1, 1, 0, 1]
k = 1

count = 0
crossword = 0

for i in a:
    if i == 1:
        count += 1
    else:
        if count == k:
            crossword += 1
        count = 0
print(crossword)