def add_students(students,name,grades):
    """添加学生"""
    students[name] = grades
    print(f"已添加:{name} - {grades}")

def search_students(students,ways):
    """查询数据"""
    if ways == "one":
        name = input("请输入被查询者姓名:").strip()
        output = students.get(name)
        if not students:
            print("无已存储数据！")
        elif output == None:
            print("无此人数据！")
        else:
            print(f"{name}的成绩是{output}。")
    elif ways == "all":
        if not students:
            print("无已存储数据！")
        for i,j in students.items():
            print(f"姓名：{i}  成绩：{j}")

def grade_average(students):
    """计算平均分"""
    if not students:
        print("无已存储数据！")
        return
    total = 0
    for i in students.values():
        total += i
    average = total/len(students)
    print(f"平均分为{average}。")

def main():
    """"主程序"""
    print("-"*30)
    print("欢迎使用学生成绩管理系统！")
    print("-"*30)
    students = {}
    while True:
        attempt = input("请选择操作！\n1,添加学生。\n2,查询数据。\n3,计算平均分。\n4,退出。\n(输入1/2/3/4)").strip()
        if attempt == "1":
            while True:
                name = input("请输入姓名:").strip()
                strgrades = input("请输入成绩：").strip()
                try:
                    grades = float(strgrades)
                except ValueError:
                    print("请正确输入成绩！")
                    continue
                add_students(students,name,grades)         
                a = input("是否继续添加(y/n)？").lower().strip()
                if a == "n":
                    break
        elif attempt == "2":
            ways = input("请选择具体服务:\n总览请输入'all'\n个人查询请输入'one'\n").strip().lower()
            search_students(students,ways)
        elif attempt == "3":
            grade_average(students)
        elif attempt == "4":
            break
        else:
            print("无效选择！")


if __name__ == "__main__":
    main()