import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


#x = np.linspace(0, 3, 20)
#y = np.linspace(0, 9, 20)

#plt.plot(x,y)
#plt.plot(x,y,'o')
#plt.show()


min0 = 0
max0 = 25



fig = plt.figure(figsize=[10,10])



images=max0*np.random.rand(20,20)



x=plt.imshow(images)


axcolor = 'lightgoldenrodyellow'


axmin = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axmax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

smin = Slider(axmin, 'Min', 10, 30, valinit=min0)
smax = Slider(axmax, 'Max', 10, 30, valinit=max0)




plt.colormaps()


plt.colorbar(x)

def update(val):
    x.set_clim([smin.val,smax.val])
    fig.canvas.draw()
smin.on_changed(update)
smax.on_changed(update)

plt.show()


