import json

def judge(prompt=None,mode=float):
    
    while True:
        try:
            a = mode(input(f'请输入{prompt}:'))
            break
        except ValueError:
            print(f'请输入正确的{prompt}:')
    return a

def judgeA(prompt=None,back=None,mode=float):

    while True:
        try:
            a = mode(input(f'请输入{prompt}:'))
            break
        except ValueError:
            print(f'请输入正确的{back}:')
    return a

def getac(ob,code):
    ac = ob.AccountHouse.get(code)
    return ac
    
class Account:
    
    def __init__(self,code,owner,key,balance=0,):
        self.owner = owner
        self.code = code
        self.key = key
        self.balance = balance
        self.status = 'normal'

    def deposit(self,amount):
        if self.status == 'freeze':
            print('交易失败！账户已被冻结。')
        else:
            self.balance += amount
            print(f'交易成功！存款{amount}。')
            return True
    
    def withdraw(self,amount,key):
        if self.key != key:
            print('密码错误！')
            return False
        if self.status == 'freeze':
            print('交易失败！账户已被冻结。')
            return False
        elif amount > self.balance:
            print(f'交易失败！余额不足。')
            return False
        else:
            self.balance -= amount
            print(f'交易成功！\n卡号{self.code}/持有人{self.owner}/余额{self.balance}')
            return True

class SavingsAccount(Account):
    
    def __init__(self, code, owner, key, balance=0):
        super().__init__(code, owner, key, balance)
        self.brand = 'save'
    
    def __str__(self):
        return f"卡号:{self.code}/密钥:{self.key}/持卡人:{self.owner}/余额:{self.balance}"
    
    def interest(self,rate):
        self.balance = self.balance * (1 + rate)

class creditAccount(Account):
    
    def __init__(self, code, owner, key, balance=0,):
        super().__init__(code, owner, key, balance)
        self.brand = 'credit'
    
    def __str__(self):
        return f"卡号:{self.code}/密钥:{self.key}/持卡人:{self.owner}/余额:{self.balance}"
    
    def withdraw(self, amount,key):
        if self.key != key:
            print('密码错误！')
            return False
        if amount > self.balance + 1000:
            print(f'交易失败！余额不足。')
            return False
        elif self.status == 'freeze':
            print('交易失败！账户已被冻结。')
            return False
        elif amount <= self.balance:
            self.balance -= amount
            print(f'交易成功！\n卡号:{self.code}/持有人:{self.owner}/余额:{self.balance}')
            return True
        else:
            deduct = amount - self.balance
            self.balance -= amount
            print(f"交易成功！信用透支{deduct}。卡号:{self.code}/持有人:{self.owner}/余额:{self.balance}")
            return True

class AccountManager:
    
    def __init__(self,code,key):
        self.admincode = code
        self.adminkey = key
        self.AccountHouse = {}
        self.Notes = {}
    
    def add(self,t,code,key,owner,balance):
        if t == 'save':
            self.AccountHouse[code] = SavingsAccount(code, owner, key, balance)
        elif t =='credit':
            self.AccountHouse[code] = creditAccount(code, owner, key, balance)
        self.save()

    def delete(self,code):
        ac = getac(self,code)
        if ac == None:
            print('操作失败！卡号不存在！')
            return False
        elif ac.balance > 0:
            print('请转移账户余额！')
            return False
        elif ac.balance < 0:
            print('请遵守信用规则还款！')
            return False
        else:
            message = self.AccountHouse.pop(code)
            self.Notes.pop(code)
            print(f'已删除{message}!')
        self.save()

    def Loading(self):
        try:
            with open('BankAccountHouse.json','r',encoding='utf-8') as f:
                house = json.load(f)
                for code1,a in house.items():
                    if a['brand'] == 'save':
                        self.AccountHouse[int(code1)] = SavingsAccount(code1,a['owner'],a['key'],a['balance'],a['status'])
                    else:
                        self.AccountHouse[int(code1)] = creditAccount(code1,a['owner'],a['key'],a['balance'],a['status'])                        
        
        except (FileNotFoundError,json.JSONDecodeError,AttributeError):
            print('无已存档账户数据！')
            return

        try:
            with open('BankNotes.json','r',encoding='utf-8') as g:
                notes = json.load(g)
                for code2,s in notes.items():
                    self.Notes[int(code2)] = s
        except (FileNotFoundError,json.JSONDecodeError):
            print('无已存档交易数据！')
            return

    def save(self):
        a = {}
        for code1,s in self.AccountHouse.items():
            a[code1] = s.__dict__
        with open("BankAccountHouse.json",'w',encoding="utf-8") as f:
            json.dump(a,f)

        b = {}
        for code2,j in self.Notes.items():
            b[code2] = j
        with open("BankNotes.json","w",encoding="utf-8") as g:
            json.dump(b,g)
    
    def note(self,code,mode,amount):
        a = getac(self,code)
        if a == None:
            print('账号不存在！')
            return False
        o = self.Notes.get(code)
        if o == None:
            self.Notes[code] = []
        else:
            pass    
        n = len(self.Notes[code])
        self.Notes[code].append(f'序号{n}/卡号{code}/交易类型{mode}/金额{amount}/余额{a.balance}')

    def search(self,code,key):
        ac = getac(self,code)
        if ac == None:
            print('卡号不存在！') 
            return False
        if ac.key != key:
            print('密码错误！')
        else:
            if type(ac) == creditAccount:
                print(f'卡号:{ac.code}/持卡人:{ac.owner}/余额:{ac.balance}')
            elif type(ac) == SavingsAccount:
                print(f'卡号:{ac.code}/持卡人:{ac.owner}/余额:{ac.balance}')

    def transfer(self,code1,key,code2,amount):
        ac1 = getac(self,code1)
        ac2 = getac(self,code2)
        if ac1 == None:
            print('转出卡卡号错误！')
            return False
        if ac2 == None:
            print('转入卡卡号错误！')
            return False
        if ac1.status == 'freeze':
            print('交易失败！转出账户已被冻结。')
            return False
        if ac2.status == 'freeze':
            print('交易失败！转入账户已被冻结。')
            return False
        amount = amount*1.01
        a = ac1.withdraw(amount,key)
        if a == False:
            return False
        ac2.balance += amount
        return True

    def interester(self,code,key):
        ac = getac(self,code)
        if type(ac) == creditAccount:
            print('该类型卡无此功能！')
            return False
        if ac.status == 'freeze':
            print('交易失败！此账户已冻结！')
            return False
        if ac.key != key:
            print('密码错误！')
            return False
        else:
            rate = judge('利率')
            orbalance = ac.balance
            ac.interest(rate)
            profit = ac.balance - orbalance
            print(f'净利:{profit}/余额{ac.balance}')
            return profit
def main():
    print("""
1.取款
2.存款
3.转账
4.结息
5.查询账户信息
6.查询交易记录
7.开卡
8.销卡
9.冻结/解冻
0.退出
""")
    service = judge('序号',int)
    if service == 1:
        code = judgeA('账号','正确的账号，形式应为纯数字！',int)
        ac = getac(account,code)
        key = input('请输入密码:')
        if ac == None:
                print('账号不存在！')
        else:
            amount = judge('金额')
            r = ac.withdraw(amount,key)
            if r == True:
                account.note(code,'取款',amount)

    elif service == 2:
        while True:
            code = judgeA('账号','正确的账号，形式应为纯数字！',int)
            ac = getac(account,code)
            if ac == None:
                print('账号不存在！')
            else:
                amount = judge('金额')
                r = ac.deposit(amount)
                if r == True:
                    account.note(code,'存款',amount)
                    break
                else:
                    break
    elif service == 3:
        code1 = judgeA('转出账号','正确的账号，形式应为纯数字！',int)
        code2 = judgeA('转入账号','正确的账号，形式应为纯数字！',int)
        amount = judge('金额')
        key = input('请输入密码:')
        r = account.transfer(code1,key,code2,amount)
        if r == True:
            account.note(code1,'转出',amount)
            account.note(code2,'转入',amount)

    elif service == 4:
        code = judgeA('账号','正确的账号，形式应为纯数字！',int)
        key = input('请输入密码:')
        ac = getac(account,code)      
        if ac == None:
            print('账号不存在！')
        else:
            amount = account.interester(code,key)
            if amount != False:
                account.note(code,'结息',amount)
    
    elif service == 5:
        code = judgeA('账号','正确的账号，形式应为纯数字！',int)
        key = input('请输入密码:')
        account.search(code,key)

    elif service == 6:
        code = judgeA('账号','正确的账号，形式应为纯数字！',int)
        adminkey = input('请输入管理员密码:')
        if account.adminkey != adminkey:
            print('密码错误！')
        else:
            notes = account.Notes.get(code)
            print(notes)

    elif service == 7:  
        while True:
            adminkey = input('请输入管理员密码:')
            if account.adminkey != adminkey:
                print('密码错误！')
            else:
                print('选择类型:\n1.储值卡\n2.信用卡')
                c = judge('序号',int)
                if c == 1:
                    code = judgeA('账号','正确的账号，形式应为纯数字！',int)
                    if getac(account,code) != None:
                        print('卡号已占用！')
                    else:
                        owner = input('请输入所有者:')
                        while True:
                            key = input('请设置密码:')
                            key1 = input('请确认密码:')
                            if key == key1:
                                print('设置成功！')
                                break
                            else:
                                print('两次密码不一致，请重试！')
                        account.add('save',code,key,owner,0)
                        break
                elif c == 2:
                    code = judgeA('账号','正确的账号，形式应为纯数字！',int)
                    if getac(account,code) != None:
                        print('卡号已占用！')
                    else:
                        owner = input('请输入所有者:')
                        while True:
                            key = input('请设置密码:')
                            key1 = input('请确认密码:')
                            if key == key1:
                                print('设置成功！')
                                break
                            else:
                                print('两次密码不一致，请重试！')
                        account.add('credit',code,key,owner,0)
                        break
                else:
                    print('请正确选择！')

    elif service == 8:
        while True:
            adminkey = input('请输入管理员密码:')
            if account.adminkey != adminkey:
                print('密码错误！')
            else:
                code = judgeA('销户账号','正确的账号，形式应为纯数字！',int)
                account.delete(code)
                break
    
    elif service ==9:     
        while True:
            adminkey = input('请输入管理员密码:')
            print('1.冻结\n2.解冻')
            a = judge('序号',int)
            if account.adminkey != adminkey:
                print('密码错误！')
            else:
                if a == 1:
                    code = judgeA('账号','正确的账号，形式应为纯数字！',int)
                    ac = getac(account,code)
                    if ac == None:
                        break
                    ac.status = 'freeze'
                    print(f'已冻结账户:{code}')
                    account.save()
                    break
                elif a == 2:
                    code = judgeA('账号','正确的账号，形式应为纯数字！',int)
                    ac = getac(account,code)    
                    if ac == None:
                        break     
                    ac.status = 'normal'
                    print(f'已解冻账户:{code}')
                    account.save()
                    break          
                else:
                    print('请正确选择！')
        
    elif service == 0:
        return 0

if __name__ == "__main__":
    print('-'*30)
    print("欢迎使用银行账户管理系统！")
    print('-'*30)
    
    manager = {}
    try:
        with open("ManagerAC.json","r",encoding='utf-8') as f:
            data = json.load(f)
            for c,s in data.items():
                manager[c] = AccountManager(c,s['key'])
    except (FileNotFoundError,json.JSONDecodeError):
        pass 
    
    while True:
        mode = judgeA('序号:\n1.立即登录\n2.立即注册','序号',int)
        if mode == 2:
            code = judgeA('管理员账号','正确的账号，形式应为纯数字！',int)
            key = input('请输入管理员密码:')
            account = AccountManager(code,key)
            manager[code] = account
            account.Loading()
            break
        elif mode ==1:
                if not manager:
                    print('暂无账户，请先注册！')
                    continue
                code = judgeA('管理员账号','正确的账号，形式应为纯数字！',int)
                key = input('请输入管理员密码:')
                account = manager.get(code)
                if account == None:
                    print('账号不存在！')
                    continue
                else:
                    if account.adminkey != key:
                        print('密码错误')
                        continue
                    elif account.adminkey == key:
                        print('登录成功！')
                        account.Loading()
                        break
    
    while True:
        a = main()
        if a == 0:
            break