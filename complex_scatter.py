import numpy as np

import matplotlib.pyplot as plt





number = 1000

x = 2 * np.random.rand(1000)
y = 2 * np.random.rand(1000)

area1=np.pi *(5 * np.random.rand(number)) **2


area2=np.pi*(5 * np.random.randn(number)) **2


c = np.sqrt(area2)
print(c)


plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)

plt.show()
