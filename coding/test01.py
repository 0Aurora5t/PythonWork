# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
# y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# ln1, = plt.plot(x_data, y_data, color='red', linewidth='2.0', linestyle='--')
# ln2, = plt.plot(x_data, y_data2, color='blue', linewidth='3.0', linestyle='-.')
# my_font=fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf")
# #添加图例的名称和位置
# plt.legend(handles=[ln2, ln1], labels=['疯狂Andeoid讲义年销量', '疯狂java讲义年销量'], loc='lower right' )
# # 调用show()函数显示图形
# plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
# plt.rcParams['axes.unicode_minus']=False
# plt.show()


import matplotlib.pyplot as plt
#准备数据
data=[0.16881,0.14966,0.07471,0.06992,0.04762,0.03541,0.02925,0.02411,0.02316,0.01409,0.36326]
#准备标签
labels=['java','C','C++','python','Visual Basic.net','C#','PHP','Javascript','SQL','Assembly langugage','其它']
ecplode=[0,0,0,0.3,0,0,0,0,0,0,0]
colors=['red','pink','magenta','purple','orange','blue']
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.axes(aspect='equal')
plt.xlim(0,8)
plt.ylim(0,8)
plt.pie(x=data,
        labels=labels,
        explode=ecplode,
        colors=colors,
        autopct='%.3f%%',
        pctdistance=0.8,
        labeldistance=1.15,
        startangle=180,
        center=(4,4),
        radius=3.8,
        counterclock=False,
        wedgeprops={'linewidth':1,'edgecolor':'green'},
        textprops={'fontsize':12,'color':'black'},
        frame=1)
plt.xticks(())
plt.yticks(())
plt.title('2018年8月的编程语言指数排行榜')
plt.show()