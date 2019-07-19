"""
# 例1
def a():
    def b():
        def c():
            nonlocal i # 由于在函数a、b中都未曾事先定义过，将报错 SyntaxError: no binding for nonlocal 'i' found
if __name__ == '__main__':
    a()
"""



# 例2
def a():
    i = 1
    def b():
        def c():
            nonlocal i # 这里绑定的i是函数a()内定义的i
            i = 3 # 将函数a内定义的局部变量i值修改为3

        c()
        print(i) # 这里访问的i是值为3的函数a内定义的局部变量

    b()
    print(i) # 这里访问的i是值为3的函数a内定义的局部变量

if __name__ == '__main__':
    i=0
    a()
    print(i) # 这里访问的i是值为0的全局内定义的全局变量i


"""
# 例3
def a():
    nonlocal i # 全局变量不可以用nonlocal绑定，会报错：SyntaxError: no binding for nonlocal 'i' found
    i=3;
    print(i)

if __name__ == '__main__':
    i=2
    a()
"""


"""
nonlocal的作用是“绑定”，而global的作用是“定义”
nonlocal绑定的变量必须事先在外层定义过（global无此要求）
全局变量不可以用nonlocal绑定
"""