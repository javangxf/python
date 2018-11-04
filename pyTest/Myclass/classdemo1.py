import abc
import random

# 定义一个抽象类


class Account(metaclass=abc.ABCMeta):
    __userName = ""
    __passWord = ""
    __balance = 0
    accountNO = ""
    acc = {}

    #构造函数
    def __init__(self,name,pw,balance):
        self.__userName = name
        self.__passWord = pw
        self.__balance = balance

    # 取钱的方法
    def drawMoney(self,num):
        print("取钱成功，账户扣款{0}".format(num))
        self.__balance -= num

    # 存钱的方法
    def saveMoney(self,num):
        print("存钱成功，账户增加{0}".format(num))
        self.__balance += num

    # 官方活动
    @abc.abstractmethod
    def activity(*self):
        pass


class ABCAcc(Account):
    '''
    ABC银行的账户
    '''
    acRecord = {}

    def __init__(self,name,pw,balance):
        super.__init__(self,name,pw,balance)
        self.accountNO = random.randrange(1000000000,9999999999)
        acc.pop(self.accountNO,self.__passWord)

    def activity(*self):
        print("暂无活动")

class ATM():
    abcAc = ABCAcc.acRecord

    def login(self,account,pw):
        if pw == abcAc.get(account):
            print("登陆成功")
        else:
            print("登陆失败,请检查账号和用户名")
            login(self,account,pw)

    def signin(self):
        ac = input("请输入用户名")
        pw1 = input("请输入密码")
        pw2 = input("请再输入密码")


 
atm = ATM()
acRecord = {1111111111:'123456',}
welcom = {1:'用户登录',2:'用户注册',3:'忘记密码',4:'锁定用户',5:'注销用户'}
welcomIndex = {1:atm.login(),2:atm.signin(),3:atm.forgetPW(),4:atm.lockUser(),5:atm.logout()}
menu = {1:'主菜单',2:'取钱',3:"存钱",4:"转账",5:"查看信息",6:"最新活动",7:"退卡"}
menuIndex = {1:menu(),2:drawMoney(),3:saveMoney(),4:transferAc(),5:info(),6:activity()}

cho = input("请输入你的选项")

name = input("请输入用户名")


print("-"*20)
# print(menu)
for key in menu:
    print("{0}:{1}".format(menu[key],key))

print("-"*20)
# print(type("xiaofeng"))
a = input("请输入你要选择的选项或内容")

# t1 = ABCATM("小凤","123456",10000)
# t1.getMoney(100)
# print(t1.__dict__)