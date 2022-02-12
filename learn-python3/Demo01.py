'''取绝对值函数:abs(),若调用函数时传入的参数不对会报TypeError的错误'''
print(abs(100))
print(abs(-32.1))
'''max函数max()可以接受任意多的参数并且返回最大的那个'''
print(max(3,7,9,34,112,23,87))
'''
数据类型转换：
    python内置的常用函数还包括数据类型转换函数，比如int（）函数可以其它数据类型转换为整型
    函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起一个
    别名
'''
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.234))
print(str(100))
print(bool(1))
print(bool(''))
a=abs
print(a(-1))
'''hex()函数可以把一个整数转换成十六进制表示的字符串'''
#print('\n')
print(hex(23))
'''
定义函数：
    在python中，定义一个函数需要使用def语句，依次写出函数名、括号、括号中参数和冒号：
    然后再缩进块中编写函数体，函数的返回值用return语句返回
'''

def my_abs(x):
    if x>= 0:
        return x
    else:
        return -x
#自定义函数的调用
print(my_abs(-99))
'''
空函数：
    如果想定义一个什么事也不做的空函数，可以用pass语句
    pass语句什么都不做，哪有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么
    写函数的代码，就可以先放一个pass，让代码能运行起来
'''
def nop(age):
    if age >= 18:
        pass
'''修改my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数，数据类型检查可以用内置函数isinstance（）实现'''
def my_abs_g(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#print(my_abs_g('yuubb'))
print(my_abs_g(679))
'''函数返回多个值'''
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)

'''
练习：
    请定义一个函数quadratic(a,b,c),接收3个参数，返回一元二次方程ax^2+bx+c=0的两个解
    提示：
        计算平方根可以调用math.sqrt()函数
'''

def quadratic(a, b, c):
    if not isinstance(a or b or c, (int, float)):
        raise TypeError("输入的数据类型不正确，请输入整数或小数")
        if a == 0:
            if b != 0:
                print("x1 = x2 = -%s/%s" % (c, b))
            else:
                return "方程无解"
        else:
            if b ** 2 - 4 * a * c < 0:
                print("方程无实根")
            else:
                x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
                x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
                return x1, x2
                print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
                print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
                if quadratic(2, 3, 1) != (-0.5, -1.0):
                    print('测试失败')
                elif quadratic(1, 3, -4) != (1.0, -4.0):
                    print('测试失败')
                else:
                    print('测试成功')
print(quadratic(2,5,7))
