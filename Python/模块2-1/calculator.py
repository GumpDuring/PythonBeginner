def get_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("请输入正确的数字！")

def gain():
    while True:
        mode = input("请选择模式:(+,-,*,/)").strip()
        if mode not in ['+', '-','*','/']:
            print('请正确输入运算符！')
        else:
            break
    num1 = get_number("请输入第一个数！")
    num2 = get_number("请输入第二个数！")
    return mode,num1,num2

def calculate(mode,num1,num2):
    if mode == "+":
        result = num1 +num2
        return result
    elif mode == "-":
        result = num1 - num2
        return result
    elif mode == "*":
        result = num1 * num2
        return result
    elif mode == "/":
        if num2 == 0:
            return "Error!0不能作为除数!"
        else:
            result = num1 /num2
            return result

def main():
    print('-'*30)
    print('欢迎使用命令行计算器！')
    print('-'*30)
    while True:
        mode,num1,num2 = gain()
        result = calculate(mode,num1,num2)
        print(f"输出:{result}")
        again = input('计算结束，键入q以退出计算！').strip().lower()
        if again == "q":
            break

if __name__ =="__main__":
    main()