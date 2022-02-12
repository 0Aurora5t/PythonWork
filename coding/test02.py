# import matplotlib.pyplot as plt
# x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
# y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# plt.plot(x_data,y_data,color='red',linewidth='2.0',linestyle='--', lable='疯狂java讲义年销量')
# plt.plot(x_data,y_data2,color='blue',linewidth='3.0',linestyle='-.',lable='疯狂Adroid讲义年销量')
# plt.legend(loc='lower right')
# import matplotlib.font_manager as fm
# my_font=fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf")
# plt.legend(loc='best')
# #设置两个坐标轴的名称
# plt.xlabel("年份")
# plt.ylabel("图书销量(本)")
# #设置数据图的标题
# plt.title('疯狂图书的历年销量')
# #设置y坐标轴上的数值文本
# #第一个参数是点的位置，第二个参数是点的文字提示
# plt.yticks([50000,70000,100000],[r'挺好',r'优秀',r'火爆'])
# #plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
# #plt.rcParams['axes.unicode_minus']=False
# plt.show()



import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
plt.figure()
# 定义从-pi到pi之间的数据，平均取64个数据点
x_data=np.linspace(-np.pi,np.pi,64,endpoint=True)
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False
# 将整个figure分成两行两列，第三个参数表示将该图形放在第一个网格中
# plt.subplot(2,1,1)
# 将绘图区域分成两行三列
gs=gridspec.GridSpec(2,3)
ax1=plt.subplot(gs[0,:])
ax2=plt.subplot(gs[1,0])
ax3=plt.subplot(gs[1,1:3])
# 绘制正弦曲线
ax1.plot(x_data,np.sin(x_data))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_position(('data',0))
ax1.spines['left'].set_position(('data',0))
ax1.set_title('正弦曲线')

# ax2.subplot(223)
# 绘制余弦曲线
ax2.plot(x_data,np.cos(x_data))
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data',0))
ax2.spines['left'].set_position(('data',0))
ax2.set_title('余弦曲线')

# plt.subplot(224)
# 绘制正切曲线
ax3.plot(x_data,np.tan(x_data))
ax3.spines['right'].set_color('red')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data',0))
ax3.spines['left'].set_position(('data',0))
ax3.set_title('正切曲线')

plt.show()