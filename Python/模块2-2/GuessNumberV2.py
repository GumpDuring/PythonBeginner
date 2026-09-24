import random

def judge(prompts):
    while True:
        try:
            num = int(input(prompts).strip())
            return num
        except ValueError:
            print('请输入正确的数字！')

def compare(num, key):
    if num > key:
        return 1
    elif num < key:
        return -1
    else:
        return 0

def get_level(CHOOSES):
    while True:
        level = input('请选择难度(键入序号):\n1,简易(1,100)\n2,中等(1,250)\n3,困难(1,500)\n4,地狱(1,1000)').strip()
        if level in CHOOSES:
            return level
        else:
            print('请输入正确的序号！')
def get_key(level,RANGES):
    return random.randint(1,RANGES[level])

def tittle(attempts,level,TITLE_RULES):
    for limit,t in TITLE_RULES[level]:
        if attempts <= limit:
            return t
    
def main():
    print('-'*40)
    print('欢迎游玩猜数字游戏！')
    print('-'*40)
    RANGES = {
        '1':100,
        '2':250,
        '3':500,
        '4':1000
    } 
    level = get_level(RANGES)
    key = get_key(level,RANGES)
    attempt = 0
    TITLE_RULES = {
        '1':[(3,'大神'),(6,'高手'),(float('inf'),'菜鸟')],
        '2':[(5,'大神'),(8,'高手'),(float('inf'),'菜鸟')],
        '3':[(7,'大神'),(12,'高手'),(float('inf'),'菜鸟')],
        '4':[(10,'大神'),(16,'高手'),(float('inf'),'菜鸟')]
    }
    while True:
        num = judge('请输入你的猜测！')
        attempt += 1
        result = compare(num, key)

        if result == 0:
            t = tittle(attempt, level,TITLE_RULES)
            print(f'恭喜你答对了！总共用了{attempt}次！获得“{t}”称号！')
            break
        elif result > 0:
            print('大了！')
        else:
            print('小了！')


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
