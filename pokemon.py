# 아래에 코드를 작성해주세요.
import random


class Pikachu:
    
    def __init__(self, name):
        self.name = name
        self.level = 5
        self.hp = self.level * random.randint(15, 20)
        self.exp = 0
        self.defense = random.randint(1, 3)
        self.evade = random.randint(0, 2)
        self.skill01 = 10
        self.skill01_name = 'bark'
        self.skill02 = 10
        self.skill02_name = 'body_attack'
        self.skill03 = 10
        self.skill03_name = 'thousond_volt'
        print(f'''
        포켓몬 정보
        이름 : {self.name}
        레벨 : {self.level}
        체력 : {self.hp}
        경험치 : {self.exp}
        방어 : {self.defense}
        회피 : {self.evade}
        ''')
        
    def bark(self, target):
        if self.skill01 < 1:
            print('기술 사용이 불가능합니다.')
        else:
            self.evade = self.evade / 4
            self.skill01 -= 1
            print(f'{self.name}은 울었다! {target.name}의 회피가 감소하였다.')
    
    def body_attack(self, target):
        if self.skill02 < 1:
            print('기술 사용이 불가능합니다.')
        else:    
            print(f'{self.name}의 몸통박치기!!')
            self.skill02 -= 1
            tmp = target.hp
            if random.choice(range(10)) in range(round(target.evade)):
                print(f'{target.name}가 공격을 회피했다!')
            else:
                target.hp -= (self.level * 5) * (self.defense / 10)
                if target.hp > 0:
                    print(f'{target.name}의 체력 : {tmp} -> {target.hp}')
                else:
                    print(f'{self.name}가 승리하였다!!')
                    self.exp += target.level * 15
                    if self.exp > self.level * 100:
                        tmp_level = self.level
                        self.level += 1
                        self.exp -= 100
                        print(f'{self.name}의 레벨이 {tmp_level} -> {self.level}로 상승하였다.')
                    else:
                        print(f'경험치가 {self.exp} (으)로 증가하였다.')
    
    def thousond_volt(self, target):
        if self.skill03 < 1:
            print('기술 사용이 불가능합니다.')
        else:    
            print(f'{self.name}의 십만볼트~!!!!!')
            self.skill03 -= 1
            tmp = target.hp
            if random.choice(range(10)) in range(round(target.evade)):
                print(f'{target.name}가 공격을 회피했다!')
            else:
                target.hp -= (self.level * 7) * (self.defense / 10)
                if target.hp > 0:
                    print(f'{target.name}의 체력 : {tmp} -> {target.hp}')
                else:
                    print(f'{self.name}가 승리하였다!!')
                    self.exp += target.level * 15
                    if self.exp > self.level * 100:
                        tmp_level = self.level
                        self.level += 1
                        self.exp -= 100
                        print(f'{self.name}의 레벨이 {tmp_level} -> {self.level}로 상승하였다.')
                    else:
                        print(f'경험치가 {self.exp} (으)로 증가하였다.')
                    
    def attack(self, target, num):
        if num == 1:
            self.bark(target)
        elif num == 2:
            self.body_attack(target)
        elif num == 3:
            self.thousond_volt(target)
            
    def npc_attack(self, target):
        skill_pool = random.choice(['bark', 'body_attack', 'thounsond_volt'])
        if skill_pool == 'bark':
            self.bark(target)
        elif skill_pool == 'body_attack':
            self.body_attack(target)
        elif skill_pool == 'thounsond_volt':
            self.thousond_volt(target)
                    
    def __del__(self):
        print(f'{self.name}가 트레이너의 품을 떠났다..')



turn = 0
p1_name = input('이름을 정해주세요 : ')
p2_name = '레드'
p1 = Pikachu(p1_name)
p2 = Pikachu(p2_name)
print('=================== 게 임 시 작 ===================')
while p1.hp > 0 and p2.hp > 0:
    turn += 1
    if turn%2:
        while True:
            print(f'''
    1. 울기 {p1.skill01}/10          2. 몸통박치기 {p1.skill02}/10
    3. 십만볼트 {p1.skill03}/10      4.                           
            ''')
            num = input('사용할 기술을 선택해주세요. :  ')
            if num == 'Q':
                raise KeyboardInterrupt
            skill_counts = [p1.skill01, p1.skill02, p1.skill03]
            if 1 <= int(num) <= 3:
                if skill_counts[int(num)-1] == 0:
                    print('\n')
                    print('사용 가능한 기술 번호를 입력해주세요.\n')
                    continue
                else:
                    break
            else:
                print('사용 가능한 기술 번호를 입력해주세요.\n')
                continue
        p1.attack(p2, int(num))
        print('\n')
    else:
        p2.npc_attack(p1)
        print('\n')