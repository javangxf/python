# PYTHON模块就是一个python文件，以.py结尾，包含了对python对象的定义和python语句
# import语句
#     模块的引用，在模块定义好后，就可以使用import语句来引入模块，
#     在调用模块中的函数的时候，必须这样引用：  模块名.函数名
#     当解释器遇到import语句，如果模块在当前的搜索路径就会被导入
#     搜索路径是一个解释器会先进行搜索的所有目录的列表，在导引模块的时候，通常把命令放在脚本顶端
#     一个模块只会被导入一次，无论执行了多少次import
# from...import语句：不会将整个模块导入当前空间，而是让你从模块中导入一个指定的部分到当前从命名空间中
# from modname import name1[,name2,[...nameN]]
# from...import * ：将一个模块的整个内容导入到当前命名空间
#
# dir()函数
#   dir()函数一个排好序的字符串列表，内容是模块定义过的名字
#   返回的列表容纳了在一个模块里定义的所有模块，变量和函数，
#   比如查看math模块下的所有模块：dir(math)
#   ['__doc__', '__loader__', '__name__', '__package__', '__spec__',
#    'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil',
#    'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1',
#    'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd',
#    'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp',
#    'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow',
#    'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
import math
print(dir(math))

# globals()和locals()函数 用来返回全局和局部命名空间里的名字
# 如果在函数内部调用locals()，返回的是所有能在函数里访问的命名
# 如果在函数内部调用globals()，返回的是所有在函数里能访问的全局名字
# 两个函数返回类型都是字典，所以他们的名字都能用keys()摘取


# reload()函数
# 当一个模块被导入到一个脚本，模块顶层部分的代码只会执行一次
# 因此，如果你想要重新执行模块顶层部分的代码，可以用reload()函数，该函数会重新导入之前导入的模块
#


# python中的包