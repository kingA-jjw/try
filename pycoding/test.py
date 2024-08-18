print('hello world')
s=0
for i in range(10):
    s+=i
print(s)
import numpy as np
a=np.array([[1,2,3],[2,3,4]])
print(a)
a=np.arange(10).reshape(5,2)
print(a)
from matplotlib import pyplot as plt
x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]
#设置图片大小
plt.figure(figsize=(20,8),dpi=80)
#绘图
plt.plot(x,y)
plt.show()
