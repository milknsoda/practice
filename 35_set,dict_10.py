alpha = input()
results = {}
for letter in set(alpha):
    results[letter] = 0
for letter in alpha:
    results[letter] = results[letter] + 1
for result in results.keys():
    print(f'{result},{results[result]}')