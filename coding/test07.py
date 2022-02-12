# import numpy as np
# import matplotlib.pyplot as plt
# def pdf(X, mu, sigma):
#     a = 1. / (sigma * np.sqrt(2. * np.pi))
#     b = -1. / (2. * sigma ** 2)
#     return a * np.exp(b * (X - mu) ** 2)
# X = np.linspace(-6, 6, 1000)
# for i in range(3):
#     samples = np.random.standard_normal(10)
#     mu, sigma = np.mean(samples), np.std(samples)
#     plt.plot(X, pdf(X, mu, sigma), color = '.66')
# plt.plot(X, pdf(X, 0., 1.), color = 'b')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# X = np.linspace(0, 2 * np.pi, 100)
# YSinValues = np.sin(X)
# YCosValues = np.cos(X)
# plt.plot(X, YSinValues)
# plt.plot(X, YCosValues)
# plt.show()
import  matplotlib.pyplot as plt
import numpy as np
plt.figure()
#定义从-pi到pi之间的数据，平均取64个数据点
x_data=np.linspace(-np.pi,np.pi,64,endpoint=True)
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False
#将整个figure分成两行两列，第三个参数表示将该图形放在第一个网格中
plt.subplot(2,1,1)
#绘制正弦曲线
plt.plot(x_data,np.sin(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data',0))
plt.gca().spines['left'].set_position(('data',0))
plt.title('正弦曲线')

plt.subplot(223)
#绘制余弦曲线
plt.plot(x_data,np.cos(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data',0))
plt.gca().spines['left'].set_position(('data',0))
plt.title('余弦曲线')

plt.subplot(224)
#绘制正切曲线
plt.plot(x_data,np.tan(x_data))
plt.gca().spines['right'].set_color('red')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data',0))
plt.gca().spines['left'].set_position(('data',0))
plt.title('正切曲线')

plt.show()