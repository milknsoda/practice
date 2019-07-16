# 1. 단어를 입력한다.
word = input()

# 2. 단어를 거꾸로 배열한다.
word_list = list(word)
rword_list = reversed(word_list)
rword = ''
for i in rword_list:
    rword = rword + i
    
# 3. 원래의 단어와 거꾸로 배열된 단어를 비교하고, 같을 경우 정해진 문장을 출력한다.
if word == rword:
    print(word)
    print('입력하신 단어는 회문(Palindrome)입니다.')