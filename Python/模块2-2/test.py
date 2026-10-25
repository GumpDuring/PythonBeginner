# ============================================================
# 学生成绩管理系统
# 运行方式: python student_manager.py
# ============================================================

import json
import os


# ============================================================
# 1. Student 类：只描述一个学生
# ============================================================
class Student:
    def __init__(self, sid, name, score):
        # sid 学号，唯一标识
        self.sid = sid
        # name 姓名
        self.name = name
        # score 成绩，浮点数
        self.score = score

    def to_dict(self):
        # 转成字典，方便存 JSON
        return {"sid": self.sid, "name": self.name, "score": self.score}

    @classmethod
    def from_dict(cls, data):
        # 从字典还原成 Student 实例
        return cls(data["sid"], data["name"], data["score"])

    def __str__(self):
        return f"学号:{self.sid:<8} 姓名:{self.name:<8} 成绩:{self.score}"

    def __repr__(self):
        return self.__str__()


# ============================================================
# 2. StudentManager 类：管理所有学生
# ============================================================
class StudentManager:
    def __init__(self, data_file="students.json"):
        # 用字典存学生，key 是学号，value 是 Student 实例
        # 字典能保证按学号查、删都是 O(1)
        self.students = {}
        # 数据文件路径
        self.data_file = data_file
        # 启动时从文件加载
        self.load()

    # --------------------------------------------------------
    # 文件持久化
    # --------------------------------------------------------
    def load(self):
        # 如果文件不存在，直接返回
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            # data 是列表，每个元素是字典
            for item in data:
                student = Student.from_dict(item)
                self.students[student.sid] = student
            print(f"已从 {self.data_file} 加载 {len(self.students)} 条学生记录")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"加载数据失败: {e}，将以空数据启动")

    def save(self):
        # 把所有学生转成字典列表，写入 JSON
        data = [s.to_dict() for s in self.students.values()]
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"已保存 {len(data)} 条记录到 {self.data_file}")

    # --------------------------------------------------------
    # 添加
    # --------------------------------------------------------
    def add(self, sid, name, score):
        if sid in self.students:
            print(f"添加失败：学号 {sid} 已存在")
            return False
        student = Student(sid, name, score)
        self.students[sid] = student
        print(f"添加成功：{student}")
        return True

    # --------------------------------------------------------
    # 删除
    # --------------------------------------------------------
    def remove(self, sid):
        if sid not in self.students:
            print(f"删除失败：学号 {sid} 不存在")
            return False
        student = self.students.pop(sid)
        print(f"删除成功：{student}")
        return True

    # --------------------------------------------------------
    # 修改
    # --------------------------------------------------------
    def update(self, sid, name=None, score=None):
        student = self.students.get(sid)
        if student is None:
            print(f"修改失败：学号 {sid} 不存在")
            return False
        if name is not None:
            student.name = name
        if score is not None:
            student.score = score
        print(f"修改成功：{student}")
        return True

    # --------------------------------------------------------
    # 按学号查
    # --------------------------------------------------------
    def query(self, sid):
        student = self.students.get(sid)
        if student is None:
            print(f"查询失败：学号 {sid} 不存在")
            return None
        print(f"查询结果：{student}")
        return student

    # --------------------------------------------------------
    # 查全部
    # --------------------------------------------------------
    def query_all(self):
        if not self.students:
            print("当前没有学生记录")
            return []
        return list(self.students.values())

    # --------------------------------------------------------
    # 按姓名模糊查
    # --------------------------------------------------------
    def query_by_name(self, keyword):
        result = [s for s in self.students.values() if keyword in s.name]
        if not result:
            print(f"没有姓名包含 '{keyword}' 的学生")
        return result

    # --------------------------------------------------------
    # 按成绩区间查
    # --------------------------------------------------------
    def query_by_score_range(self, low, high):
        result = [s for s in self.students.values() if low <= s.score <= high]
        if not result:
            print(f"没有成绩在 [{low}, {high}] 区间的学生")
        return result

    # --------------------------------------------------------
    # 按成绩排序
    # --------------------------------------------------------
    def sort_by_score(self, reverse=True):
        return sorted(self.students.values(), key=lambda s: s.score, reverse=reverse)

    # --------------------------------------------------------
    # 统计
    # --------------------------------------------------------
    def stats(self):
        if not self.students:
            print("当前没有学生记录，无法统计")
            return
        scores = [s.score for s in self.students.values()]
        print(f"总人数  : {len(scores)}")
        print(f"平均分  : {sum(scores) / len(scores):.2f}")
        print(f"最高分  : {max(scores)}")
        print(f"最低分  : {min(scores)}")


# ============================================================
# 3. 命令行交互界面
# ============================================================
def print_menu():
    print("\n" + "=" * 40)
    print("        学生成绩管理系统")
    print("=" * 40)
    print("  1. 添加学生")
    print("  2. 删除学生")
    print("  3. 修改学生")
    print("  4. 按学号查询")
    print("  5. 查询全部")
    print("  6. 按姓名查询")
    print("  7. 按成绩区间查询")
    print("  8. 按成绩排序")
    print("  9. 统计信息")
    print("  s. 保存数据")
    print("  0. 保存并退出")
    print("=" * 40)


def input_float(prompt):
    # 循环直到用户输入合法数字
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("请输入合法数字")


def main():
    manager = StudentManager()

    while True:
        print_menu()
        choice = input("请选择操作: ").strip()

        # ---- 1. 添加 ----
        if choice == "1":
            sid = input("学号: ").strip()
            if not sid:
                print("学号不能为空")
                continue
            name = input("姓名: ").strip()
            if not name:
                name = "未命名"
            score = input_float("成绩: ")
            manager.add(sid, name, score)

        # ---- 2. 删除 ----
        elif choice == "2":
            sid = input("要删除的学号: ").strip()
            manager.remove(sid)

        # ---- 3. 修改 ----
        elif choice == "3":
            sid = input("要修改的学号: ").strip()
            if sid not in manager.students:
                print(f"学号 {sid} 不存在")
                continue
            new_name = input("新姓名（直接回车跳过）: ").strip()
            new_score_str = input("新成绩（直接回车跳过）: ").strip()

            new_name = new_name if new_name else None
            new_score = float(new_score_str) if new_score_str else None

            manager.update(sid, new_name, new_score)

        # ---- 4. 按学号查 ----
        elif choice == "4":
            sid = input("学号: ").strip()
            manager.query(sid)

        # ---- 5. 查全部 ----
        elif choice == "5":
            students = manager.query_all()
            for s in students:
                print(s)

        # ---- 6. 按姓名查 ----
        elif choice == "6":
            keyword = input("姓名关键字: ").strip()
            results = manager.query_by_name(keyword)
            for s in results:
                print(s)

        # ---- 7. 按成绩区间查 ----
        elif choice == "7":
            low = input_float("最低分: ")
            high = input_float("最高分: ")
            results = manager.query_by_score_range(low, high)
            for s in results:
                print(s)

        # ---- 8. 排序 ----
        elif choice == "8":
            order = input("升序还是降序？(a=升序, d=降序，默认降序): ").strip().lower()
            reverse = (order != "a")
            students = manager.sort_by_score(reverse=reverse)
            if not students:
                print("当前没有学生记录")
            for s in students:
                print(s)

        # ---- 9. 统计 ----
        elif choice == "9":
            manager.stats()

        # ---- s. 保存 ----
        elif choice.lower() == "s":
            manager.save()

        # ---- 0. 退出 ----
        elif choice == "0":
            manager.save()
            print("已退出，数据已保存")
            break

        else:
            print("无效选项，请重新输入")


# ============================================================
# 4. 程序入口
# ============================================================
if __name__ == "__main__":
    main()