import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data_gen():
    t = data_gen.t
    cnt = 0
    while cnt < 1000:
        cnt+=1
        t += 0.05
        yield t, 1.1 + np.sin(2*np.pi*t) * np.exp(t/10.)
data_gen.t = 0

plt.rc ('grid', color='g', lw=1, ls='-')
plt.rc ('xtick', labelsize=15, color='b')
plt.rc ('ytick', labelsize=15, color='b')
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_axes([.05, .90, .9, .08], polar=False,  xticks=[], yticks=[])
ax2 = fig.add_axes([.05, .05, .9, .8], polar=True)
#ax = fig.add_axes([.1,.1,.8,.8], polar=False, axisbg='k')
line, = ax2.plot([], [], lw=2)
ax2.set_ylim(0, 2.2)
ax2.set_xlim(0, 140)
ax2.grid(1)
xdata, ydata = [], []
title = ax1.text (0.02, 0.5, '', fontsize=14, transform=ax1.transAxes)

def init():
    line.set_data([], [])
    title.set_text ('')
    return line, title

def run(data):
    # update the data
    t,y = data
    xdata.append(t)
    ydata.append(y)
    ymin, ymax = ax2.get_ylim()

    if y >= ymax:
        ax2.set_ylim (ymin, 2*ymax)
        ani._blit_cache.clear() # <- add to clear background from blit cache
        title.set_text('') # <- eliminate text artifact in title
        ax2.figure.canvas.draw()

    title.set_text ("time = %.3f, y(t) = 1.1 + sin(2*pi*t) + exp(t/10) = %.3f" % (t, y))
    line.set_data(xdata, ydata)
    return line, title

ani = animation.FuncAnimation(fig, run, data_gen, init, blit=True, interval=100, repeat=False)
ani.save("cardiod23.mp4")

plt.show()