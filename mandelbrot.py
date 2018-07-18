import numpy as np 
import matplotlib.pyplot as pl 
from matplotlib.widgets import Slider
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter


def mandelbrot(complex_num,max):
	z = complex_num
	for n in range(max):
		if abs(z)>2 :
			return n
		z = z*z + complex_num

	return 0



def man_set(x_min,xmax,y_min,y_max,width,height,max):
	row1=np.linspace(x_min,xmax,width)
	row2=np.linspace(y_min,y_max,height)
	n=np.empty((width,height))

	for i in range(width):
		for j in range(height):
			n[i,j]=mandelbrot(row1[i] +1j*row2[j],max)
	return(n)




x= man_set(-2.0,0.5,-1.25,1.25,500,500,500)

fig = pl.figure(figsize=(40,40))
ims = [] 


for i in range(2):
	im =pl.imshow(x,animated=True)
	ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True,
                                repeat_delay=5)


pl.colormaps()
pl.hot()

pl.savefig("mandelbrot.jpg")

pl.show()
