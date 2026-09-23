def GuessNumber():
    print('-'*30)
    print('欢迎游玩猜数字游戏！')
    print('-'*30)
    #难度选择，获取谜底
    import random
    choose = input("请选择难度:\n1,简易\n2,中等\n3,困难\n输入（1/2/3）:").strip()
    while True:
        if choose  == "1":
            secret = random.randint(1,100)
            break
        elif choose == "2":
            secret = random.randint(1,200)
            break
        elif choose == "3":
            secret = random.randint(1,500)
            break
        else:
            choose = input("请输入数字1/2/3!").strip() 
    #输入key，并定义attempt，游戏主程序
    attempt = 0
    while True:
        key = input("请输入你的猜测:").strip()
        try:
            a = int(key)
            attempt += 1
            if a == secret:
                print("恭喜你猜对了！")
                if attempt <= 3:
                    tittle = "大神"
                elif attempt <= 8:
                    tittle = "高手"
                else:
                    tittle = "菜鸟"
                print(f"共猜了{attempt}次!获得{tittle}称号!")
                break                   
            elif a > secret:
                print("太大了！")
            elif a < secret:
                print("太小了！")
        except ValueError:
            print("请输入一个整数！")
#程序入口
def main():
    GuessNumber()
    while True:
        again = input("是否继续游玩？y/n:").strip().lower()
        if again not in ['y','n']:
            print('请输入y/n！')
        elif again == "n":
            print("欢迎再次游玩！")
            break
        else:
            GuessNumber()
if __name__ == "__main__":
    main()
            
