import math
x = '???'
print(x)

print("hello world");
# 集合数组的倒序与正序
# 0为正序的第一个，1为第二个，以此类推
# -1为倒序的第一个，-2为第二个，以此类推
# List 相当于数组方法有append追加，insert插入，pop移除，替换（赋值）
l = ['admam','lisa','paul','bart']
l.pop(3)
l.pop(2)
print(l)

# tuple 有序列表，相当于元组，没有append，pop，insert等方法，可通过下标来获取元素
# 当tuple里只有一个元素的时候（创建单元素tuple），要在元素后加‘，’避免歧义
# 当tuple包含list的时候，可导致tuple的元素是可变的
t = ('admam','lisa','paul','bart')

# python的代码缩进原则：具有相同缩进的代码被视为代码块
# 缩进严格按照python的习惯写法：四个空格，不要使用tab，更不要混合tab和空格，
#  当在python交互环境下敲代码，要留意缩进，退出缩进要多按一行回车
# if后接表达式，然后用：表示代码块的开始
grade = 75
if( grade > 60):
    print('及格')
else:
    print('不及格')

if(grade > 90):
    print('非常好')
else:
    if(grade > 60):
        print('及格')
        print('还得加油')
    else:
        print('重修吧，孩子啊')

# 对集合的遍历
for name in l:
    print(name)
print()
for t1 in t:
    print(t1)

# while循环 布尔类型的True 与 False首字母大写
#  while True:
#      print(l[0])
    #  l.pop(l[0])
    #  print('溢出成功')

# 多重循环
for i in  range(1,10):
    for j in range(1,i):
        print("此处多重循环")
        #  print(i+'*'+j+'='+i*j)

# dict{}相当于java的map存放的是一对key-value键值对，由于dict也是集合，所以len()函数可以计算任意集合的大小
d = {
    'paul':30,
    'adam':95,
    'bart':86,
    #  l:42,
}
#  对dict的访问，可以使用d（集合名）[key]返回值为value，与list比较像，list必须使用索引返回相应的元素，而dict使用key()
#  如果key不存在，会直接报错：keyError，
#  要避免该错的发生，有两个办法1.使用in操作符判断key是否存在。2.使用提供的get方法，若不存在则返回None
#  优点：查找速度快；存储key-value顺序对的时候无无序；作为key的元素必须是不可变的，否则报错：unhashable type
# dict更新信息
d['paul'] = 100
print(d)

#  遍历dict:遍历所有的key，然后通过key来获得value
for key in d:
    print(key)

print('-------------------------------------------------------')
#  set集合，里面不能包含重复的元素，无序的
s = set(['adma','lisa'])
# 对set集合访问用in
print('lisa' in s)

print('-------------------------------------------------------')
#  对越set的集合的遍历与其他集合遍历一致
for s1 in s:
    print(s1)

print('-------------------------------------------------------')
#  set更新
#  1.增加元素add()，如果增加的元素已经存在，则不会报错，但也不会增加进去
s.add('bob')
#  2.删除元素remove(),如果被删除的元素不存在，则报错，因此在进行删除元素操作之前最好进行判断操作
print(s)
print (s.remove('lisa'))
print(s)

print('-------------------------------------------------------')
#  函数
#  内置函数：
#    abs()取绝对值;
#    int()将其他类型转换为int;
#    str()将其他类型转换为字符串;
#    cmo(x,y)比较两个值的大小;
#    sum(x,y)求和
print(abs(-20))

print('-------------------------------------------------------')
# 函数的定义
# 定义函数使用def语句，依次写出函数名，括号，括号中的参数和冒号，
# 然后在缩进块中编写方法体，函数的返回值用return语句返回,
# 没有return语句，函数执行完毕后也会返回结果，只是结果为None，return None可简写为return
# def sum1(a,b):
#   c = a+b
#   return c
def sum1(a,b):
  c = a+b
  return c
print(sum1(1,3))


print('-------------------------------------------------------')
# 如何返回多值
# return a,b
# 其实返回多值的时候是返回由这几个多值组成的tupe，在语法上返回一个tupe可以省略括号
def sumAndmul(a,b):
    c = a+b
    d = a*b
    return c,d
print(sumAndmul(4,6))

print('-------------------------------------------------------')
# 函数递归  举例求n阶乘
def fac(n):
    if n==1:
        return n
    else:
        return n*fac(n-1)

print(fac(10))


print('-------------------------------------------------------')
# 定义默认参数,在定义函数的时候将其中的某（几）个设置为常量
# 由于函数的参数是从左往右匹配的，故在定义默认参数的时候默认参数必须定义在必需参数后面
# def sum(a,10):
#   pass
#  sum(10)

print('-------------------------------------------------------')
# 定义可变参数，在可变参数前加个*，表示我们可以传入0个，1个或多个参数给可变参数
# python解释器会将这一组参数组装成一个tuple传递给可变参数，
# 因此在函数内部，可变参数就是一个tuple
# 例如    def fn(*args):
#            print args
def average(*arr):
    print(arr)
    s=0.0
    for a in arr:
        print(a)
        s += a
    print(len(arr))
    print(s)
    print(s/len(arr))

average(1,2,3,4,5,6,7,8,10)


print('-------------------------------------------------------')
# 对list进行切片（支持倒序）
# l[1:3]表示从索引1开始取，直到索引3为止但不包括索引3即索引1，2，成为一个新的list
# 如果第一个索引为0，还可以省略
# l[:]表示从头取到尾
# l[::n]表示每n个取一个，也就是每隔n-1个取一个
# 把list换成tuple，切片操作完全相同，只是切片的结果也成了tuple
l.append('bob')
l.append('julia')
print(l[1:3])     # 表示从索引1开始取，直到索引3为止但不包括索引3即索引1，2，如果第一个索引为0，还可以省略


print('-------------------------------------------------------')
# 切片操作支持对字符串操作
# .upper() 将字符串转换成大写的
def firstCharUpper(s):          #将传入的字符串首字母大写

    s1 = s[1:].upper()
    return s[0:1].upper()+s[1:]

print(firstCharUpper('hello'))
print(firstCharUpper('sunday'))
print(firstCharUpper('september'))


print('-------------------------------------------------------')
# python的for循环抽象程度高于java
# 集合是指包含一组元素的数据结构
# 有序集合：list，tuple，str和Unicode
# 无序集合：set
# 无序集合并具有key-value键值对的：dict
# 内置函数range(a,b[,c])




print('-------------------------------------------------------')
# 异常捕捉
# try:
#   代码块
# except 异常名1:
#     处理1
# except 异常名2:
#     处理2
# except Exception:
#     处理
# finally:
#   最终执行语句



print('-------------------------------------------------------')
# 自定义异常
def fun(a):
    c = 0;
    c = math.log(a)
    print(c)
fun(0)