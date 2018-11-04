import math
# 异常类
# 常用的异常：
# BaseException 所有异常的基类
# Exception 常规错误的基类
# OverflowError 数值运算超过最大值
# ZeroDivisionError  除零
# AttributeError  对象没有这个属性
# ImportError  导包错误
# NameError  未声明/初始化对象（没有属性）
# UnboundLocalError  访问未初始化的本地变量
# TabError  tab与空格混用
# 。。。。
def fun(a):
    # try:

        print(math.log(a))
        # print('有错')
        # print(Exception)
fun(0)