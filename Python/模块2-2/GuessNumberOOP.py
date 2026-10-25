import random
class Game:
    def __init__(self,level,RANGES):
        self.key = random.randint(1,RANGES[level])
        self.attempt = 0
        self.level = level
    
    def guess(self,num):
        self.attempt += 1
        if num > self.key:
            return 1
        elif num < self.key:
            return -1
        else:
            return 0

    def title(self):
        RULES = {
            '1':[(3,'大神'),(6,'高手'),(float('inf'),'菜鸟')],
            '2':[(5,'大神'),(8,'高手'),(float('inf'),'菜鸟')],
            '3':[(7,'大神'),(12,'高手'),(float('inf'),'菜鸟')],
            '4':[(10,'大神'),(16,'高手'),(float('inf'),'菜鸟')]
            }
        for limit,t in RULES[self.level]:
            if self.attempt <= limit:
                return t,self.attempt

def main():
    print('8'*30)
    print("欢迎游玩猜数字游戏！")
    print('8'*30)
    RANGES = {
    '1':100,
    '2':250,
    '3':500,
    '4':1000
    }
    while True:
        level = input('请选择难度(键入序号):\n1,简易(1,100)\n2,中等(1,250)\n3,困难(1,500)\n4,地狱(1,1000)').strip()
        if level in RANGES:
            break
        else:
            print('请输入正确的序号！')
    g = Game(level,RANGES)
    while True:
        try:
            num = int(input('请输入你的猜测：'))
            result = g.guess(num)
            if result == 1:
                print('大了')
            elif result == -1:
                print('小了')
            else:
                title,attempt = g.title()
                print(f'恭喜你答对了！共尝试{attempt}次，获得"{title}"称号！')
                break
        except ValueError:
            print('请正确输入整数！')

if __name__ == "__main__":
    main()
    while True:
        again = input("是否继续游玩？(y/n)").strip().lower()
        if again == 'y':
            main()
        elif again == 'n':
            print('欢迎下次游玩！')
            break
        else:
            print('请正确输入(y/n)！')