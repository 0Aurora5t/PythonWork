def division():
    '''功能：分苹果'''
    print("\n====================分苹果======================\n")
    for i in range(0, 100):
        apple = int(input("请输入苹果的个数："))
        children = int(input("请输入来了几个小朋友："))
        if apple < children:
            assert apple>children,"苹果不够分"
        result = apple // children
        remain = apple - result * children
        if remain > 0:
            print(apple, "个苹果，平均分给", children, "个小朋友，每人分", result, "个，剩下", remain, "个")
        else:
            print(apple, "个苹果，平均分给", children, "个小朋友，每人分", result, "个")
    print("==============================================")


if __name__ == '__main__':
    try:
      division()
    except AssertionError as e:
        print("\n 输入有错误：",e)