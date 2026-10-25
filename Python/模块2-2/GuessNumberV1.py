def again(a):
    while True:
            ag = input("是否继续？(y/n):").strip().lower()
            if ag == "y":
                a()
            elif ag  == "n":
                break
            else:
                print("请输入y或n！！")
def GuessNumber():
    print("-"*30)
    print("   欢迎游玩猜数字游戏！")
    print("-"*30)
    import random
    num = random.randint(1,101)
    while True:
        s = input("请输入一个整数：")
        try:
            num1 = int(s)
            if num1 < num:
                print("小了")
            elif num1 > num:
                print("大了")
            else:
                print(f"恭喜你，猜对了！答案是{num}！")
                break
        except ValueError:
            try:
                float(s)
                print("你输入的是小数，请输入整数！")
            except ValueError:
                print("类型错误！请输入一个整数！")
if __name__ == "__main__":
    GuessNumber()
    again(GuessNumber)
    print("欢迎下次游戏！")
