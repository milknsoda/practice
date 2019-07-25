n = int(input())
for i in range(n):
    line = []
    for k in range(i+1):
        if k == 0 or k == i:
            line.append(1)
        elif i > 1:
            line.append(line_a[k-1] + line_a[k])
    line_a = list(line)
    string = ''
    for idx, num in enumerate(line):
        string += str(num)
        if idx != len(line)-1:
            string += ' '
    print(string)