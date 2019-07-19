def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    print(b)  # NameError: name 'b' is not defined
    foo()

"""
没有定义的变量无法访问（NameError: name xxx is not defined）

在全局中定义的变量为全局变量，属于全局作用域。
在函数中定义的变量为局部变量，属于局部作用域。
在函数中A中嵌套的函数B中定义的变量，B为该变量的局部作用域，A为该变量的嵌套作用域。

Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索。
"""
