words = input().split()

words = set(words)
words = sorted(list(words))
words = ",".join(words)
print(words)