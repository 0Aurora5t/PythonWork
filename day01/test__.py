for i in range(1000000000):
  s=input("请输入除数：")

  try:
    result=20/int(s)
    print("20除以%s的结果是：%g"%(s,result))
  except ValueError:
    print("值错误，您必须输入数字：")
  except ArithmeticError:
    print("算术错误，您不能输入0")
  else:
    print("没有异常出现")