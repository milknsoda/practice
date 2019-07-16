# 리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해보시오.
# 이때 리스트 내포 기능을 사용하여, 원소의 공백은 제거한다.
# 0. 리스트를 생성한다.
fruits = ['   apple    ','banana','  melon']
# 1. 리스트 내포 기능을 이용하여 각 원소의 공백을 제거한다.
name = {}
for fruit in fruits:
    apple = ''
    for i in fruit:
        if i != ' ':
            apple = apple + i
# 2. 공백을 제거한 원소를 키로 하고, 그 length를 값으로 하는 딕셔너리를 만든다.            
    name[apple] = len(apple)
print(name)