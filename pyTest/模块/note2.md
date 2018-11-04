1.模块

    一个模块就是一个包含python代码的文件，后缀名是.py就可以，模块就是个python文件
   为什么使用模块
   
        -程序太大，编写维护不太方便，需要拆分
        可以增加代码重复利用的方式
        当做命名空间使用，避免命名冲突
        
   定义模块
   
        模块就是个普通的文件，所以任何代码可以直接书写
        不过根据模块的规范，最好在模块中编写以下内容
            1.函数（单一功能）
            2.类（相似功能的组合，类似业务模块）
            3.测试代码
            
   如何使用模块
    
            import 模块名
            模块名.方法名
            模块名.类名
            借助于外部第三方的importlib包，便可实现导入以数字开头的模块名称
            import importlib
            变量名 = importlib.import_module("01")       #导入模块名为01的模块
      
   模块的搜索顺序：
   
        1.内存里的模块4
        2.python内置的模块
        3.sys.path下的模块

2.包

    一个.py文件的文件夹，里面一定含有__init__.py文件，否则系统默认为一个普通的文件夹
   导包：
        import package_name         将包导入当前文件
        使用__init__.py方法：
            package_name.fun_name()
            package_name.class_name()
        from package_name import module_name   从包中导入指定的模块
        此方法不执行__init__.py的内容

        from package_name import *             导入包中__init__文件的所有内容（函数，类等）

        导入包中的所有的模块

        __all__的用法
        在使用from package import * 的时候，*可以导入的内容
        如果在__init__文件中没有定义__all__的内容，或者该文件为空,那么只可以把'__init__'的内容导入
        如果在__init__文件中定义了__all__的值，则如上定义的时候，则会按照'__all__'指定的子包或者模块进行加载，
        如此则不会加载__init__的内容