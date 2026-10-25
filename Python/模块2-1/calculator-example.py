# calculator.py
# 命令行计算器 - 模块2第1周项目

def calculator():
    """命令行计算器主函数"""
    print("=" * 30)
    print("   欢迎使用命令行计算器")
    print("=" * 30)
    
    # 获取第一个数字
    # 使用 try-except 处理输入错误（这是异常处理，本周只要求理解，不要求自己写）
    try:
        num1 = float(input("请输入第一个数字: "))
    except ValueError:
        print("❌ 错误：请输入有效的数字！")
        return
    
    # 获取运算符
    operator = input("请输入运算符 (+ - * /): ").strip()
    
    # 验证运算符
    if operator not in ['+', '-', '*', '/']:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        print("❌ 错误：无效的运算符！")
        return
    
    # 获取第二个数字
    try:
        num2 = float(input("请输入第二个数字: "))
    except ValueError:
        print("❌ 错误：请输入有效的数字！")
        return
    
    # 计算结果
    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("❌ 错误：除数不能为0！")
            return
        result = num1 / num2
    
    # 输出结果
    print(f"\n✅ 计算结果: {num1} {operator} {num2} = {result}")
    
    # 判断结果特性（额外练习）
    if result == int(result):
        print(f"   这是一个整数: {int(result)}")
    else:
        print(f"   这是一个小数，保留2位: {result:.2f}")


# 程序入口
if __name__ == "__main__":
    calculator()
    
    # 询问是否继续
    while True:
        again = input("\n是否继续计算? (y/n): ").strip().lower()
        if again == 'y':
            calculator()
        elif again == 'n':
            print("感谢使用，再见！")
            break
        else:
            print("请输入 y 或 n")