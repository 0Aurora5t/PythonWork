import matplotlib.pyplot as plt
#定义两个列表分别作为x坐标轴、y坐标轴
#x_data=['2011','2012','2013','2014','2015','2016','2017']
#y_data=[58000,60200,63000,71000,84000,90500,107000]
#第一个列表代表横坐标的值，第二个列表代表纵坐标的值
#plt.plot(x_data,y_data)
#plt.plot(x_data)
#调用show()函数显示图形
#plt.show()
x_data=['2011','2012','2013','2014','2015','2016','2017']
y_data=[58000,60200,63000,1000,84000,90500,107000]
y_data2=[52000,54200,51500,58300,56800,59500,62700]
ln1,=plt.plot(x_data,y_data,color='red',linewidth='2.0',linestyle='--')
ln2,=plt.plot(x_data,y_data2,color='blue',linewidth='3.0',linestyle='-.')
plt.legend(handles=[ln2,ln1],labels=['疯狂Anddroid 讲义年销','疯狂java讲义年销'],loc='lower right')
#plt.plot(x_data,y_data)
#plt.plot(x_data,y_data2)
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.show()