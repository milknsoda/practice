# 임의의 URL을 받아 protocol, host, 나머지로 구분하는 프로그램
# 1. URL을 입력받는다.
url = input()

# 2. URL을 protocol, host, 나머지로 나눈다.
head = url.find('://')
mid = url.find('/', head + 3)
protocol = ''
host = ''
etc = ''

for i in range(head):
    protocol += url[i]

for i in range(head + 3, mid):
    host += url[i]

for i in range(mid + 1, len(url)):
    etc += url[i]


# 3. 양식에 맞게 출력한다.
print(f'protocol: {protocol}')
print(f'host: {host}')
print(f'others: {etc}')