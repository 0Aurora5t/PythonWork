import xlrd
import xlwt
# xslx=xlrd.open_workbook("d:七月下旬入库表.xlsx")
# print(xslx)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # 对象中的方法
    def myFunction(self):
            print("Hello my name is "+self.name)
p1 = Person("zhangsan",18)
print(p1.name)
print(p1.age)
p1.myFunction()
class Job:
    def __init__(self,wenyuan,xingzheng,xiaoshou,changping):
        self.wenyuan=wenyuan
        self.xingzheng=xingzheng
        self.xiaoshou=xiaoshou
        self.chanping=changping
    def myFun(self):
        if(self.wenyuan=="chanping1"):
            print("Welcome too you "+self.wenyuan)
        else:
            print("go back too you!")
j1=Job("wenyuan1","xingzheng1","xiaoshou1","chanping1")
j2=Job("wenyuan2","xingzheng2","xioashou2","chanping2")
print(j1.wenyuan+","+j1.xingzheng+","+j1.xiaoshou+","+j1.chanping)
print(j2.wenyuan+","+j2.xingzheng+","+j2.xiaoshou+","+j2.chanping)
j1.myFun()
j2.myFun()
class Test:
    def __init__(self):
        print("wellcome")


def TestArea(baseup,basedown,height):
    area=(baseup+basedown)*height/2
    print(area)
TestArea(5,5.7,4.5)
xslx=xlrd.open_workbook("C:\Users\沉默小多数\Desktop\工作文档\分区域导出饱和收入表.xlsx")
table=xslx.sheet_by_index(0)
value=table.cell_value(2,6)
print(value)

new_workBook=xlwt.Workbook()
work_sheet=new_workBook.add_sheet("new_test")
work_sheet.write(0,0,"test")
new_workBook.save("d:/teat.xslx")