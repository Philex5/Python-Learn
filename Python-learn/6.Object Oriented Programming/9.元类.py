"""
   动态语言和静态语言最大的不同：就是函数和类的定义，不是编译时定义的，
                            而是运行时动态创建的

   因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

    Hello = type('Hello', (object,), dict(hello=fn))
      1. class的名称；
      2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
      3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
"""
"""
    metaclass（元类）：允许创建或者修改类
                     先定义metaclass， 就可以创建类，最后创建实例 
      
"""
