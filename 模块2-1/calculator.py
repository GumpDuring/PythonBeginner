def calculator():
    print("_"*30)
    print("欢迎使用命令行计算器")
    print("_"*30)
    #获取第一个数
    try:
        num1 = float(input("请输入第一个数字:").strip())
    except ValueError:
        print("请输入正确的数字！")
        return
    #获取计算符
    print("请输入运算符(+ - * /):")
    operator = input().strip()
    if operator not in ['+','-','*','/']:
        print("运算符错误！")
        return
    #获取第二个数
    try:
        num2 = float(input("请输入第二个数字:").strip())
    except ValueError:
        print("请输入正确的数字！")
        return
    #计算
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("零不能做除数！")
            return
        else:
            result = num1 / num2
    print(f"计算结果为：{num1} {operator} {num2} = {round(result,2)}")
    if abs(result - int(result)) <= 1e-10:
        print("这是一个整数")
    else:
        print("这是一个小数")
#程序入口
if __name__ == "__main__":
    calculator()
    while True:
        again = input("是否继续计算？(y/n):").strip().lower()
        if again == "y":
            calculator()
        elif again  == "n":
            break
        else:
            print("请输入y或n！！")