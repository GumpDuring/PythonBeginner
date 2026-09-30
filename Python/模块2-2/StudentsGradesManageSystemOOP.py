import json

def judge(prompt=None,mode=float):
    while True:
        try:
            a = mode(input(f'请输入{prompt}:'))
            break
        except ValueError:
            print(f'请输入正确的{prompt}:')
    return a

class Student:
    def __init__(self,code,name,grades):
        self.name = name
        self.grades = grades
        self.code = code

    def __str__(self):
        return f"学号{self.code} 姓名{self.name} 成绩{self.grades}"
    
class StudentManager:
    def __init__(self,name):
        self.students = {}
        self.name = name
        self.load()
    
    def load(self):
        try:
            with open('studentgrades.json','r',encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            print('无已存档数据！')
            return
        
        for code ,s in data.items():
            self.students[code] = Student(s['code'],s['name'],s['grades'])

    def save(self):
        data = {}
        for code,s in self.students.items():
            data[code] = s.__dict__
        
        with open('studentgrades.json','w',encoding='utf_8') as f:
            json.dump(data,f)
    
    def add(self,code,name,grades):
        if code in self.students:
            print(f'添加失败！学号{code}已存在！')
            return False
        
        student = Student(code,name,grades)
        self.students[code] = student
        print(f'添加成功：{student}')
        print(self.students)
        self.save()
    
    def remove(self,code):
        if code not in self.students:
            print(f'删除失败！学号{code}不存在！')
            return False
        
        student = self.students.pop(code)
        print(f'删除成功：{student}')
        self.save()
   
    def search(self,code):
        student = self.students.get(code)
        if student == None:
            print('无结果')
            return False
        print(f'查询成功：{student}')

    def search_all(self):
        if not self.students:
            print('无成绩数据！')
            return False
        
        for s in self.students.values():
            print(s)
    
    def change(self,code,grades=None,name=None):
        student = self.students.get(code)
        if student == None:
            print(f'修改失败！不存在学号{code}')
            return False
        
        if grades != None:
            student.grades = grades
        
        if name != None:
            student.name = name
        print('执行完毕')
        self.save()
    
    def average(self):
        if not self.students:
            average = 0
        
        total,counts = 0,0
        for i in self.students.values():
            j = i.grades
            total += j
            counts += 1
        average = total / counts
        print(average)
    
def main():
    print(""""服务目录:
1.添加学生
2.删除学生
3.修改数据
4.查询学生
5.查询所有
6.计算平均数
0.退出   """)
    service = judge('序号',int)
    print('-'*30)
    print('-'*30)

    if service == 1:
        code = input('请输入学号:')
        name = input('请输入姓名:')
        grades = judge('成绩')
        manager.add(code,name,grades)
    
    elif service == 2:
        code = input('请输入学号:')
        manager.remove(code)
    
    elif service == 3:
        code = input('请输入学号:')
        print('请选择修改的内容:\n1.姓名\n2.成绩\n3.全部')
        choice = judge('序号',int)
        if choice == 1:
            name = input('请输入姓名:')
            manager.change(code,name=name)
        
        elif choice == 2:
            grades = judge('成绩')
            manager.change(code,grades=grades)
        
        else:
            name = input('请输入姓名:')
            grades = judge('成绩') 
            manager.change(code,name=name,grades=grades)
    
    elif service == 4:
        code = input('请输入学号:')
        manager.search(code)
    
    elif service == 5:
        manager.search_all()

    elif service == 6:
        manager.average()

    elif service == 0:
        return 0
    
if __name__ == '__main__':
    print('-'*30)
    print('-'*30)
    print('欢迎使用学生成绩管理系统！')
    print('-'*30)
    manager = StudentManager('1')
    while True:
        a = main()
        if a == 0:
            break
