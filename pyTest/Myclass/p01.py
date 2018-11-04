# 定义学生类
# 定义一个空类
class Student():
    # 一个空表，pass代表跳过，pass必须有
    pass

#定义一个对象
xiaofeng = Student()


class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    def __init__(self):
        pass


    # 注意
    #     缩进层级
    #     系统默认有一个self参数
    def doHomeWork(self):
        print(self.age)
        print("正在做作业")
        return None

    def doAgain():
        print(__class__.age)


# lei = PythonStudent()
# lei.doHomeWork()
# lei.doHomeWorkAgain()

# PythonStudent.doHomeWork()
# print(lei.__dict__)
# print(PythonStudent.__dict__)



class Person():
    name = "noName";
    age = 0;
    def sleep(self):
        print("sleep")

class Teacher(Person):
    pass

t = Teacher()
print(t.name)
print(Teacher.name)
print(issubclass(Teacher,Person))