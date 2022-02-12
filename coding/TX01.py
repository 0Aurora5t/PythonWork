from pylab import *
import matplotlib.pyplot as plt
colums_x = ['aa','bc','ad','bd']
colums_y = [12,14,10,15]
# 自定义 x轴 的取值：
plt.xticks(arange(len(colums_x)),colums_x)
# 不要再写进 colums_x 了
plt.plot(colums_y)
plt.show()