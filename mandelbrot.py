# 18.06.2020
#
# Mandelbrot fractal

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of pixels per side:
npixels = 1000

xtarget = -0.75
ytarget = 0.1
rad = 2

def sisosig(x,y):
    itmax = 500 #maximum number of iterations
    zlimit = 100 #norm that divides the complex plane
    c = complex(x,y)
    z = complex(0,0)
    n = 0
    for i in range(itmax):
        z = z**2 + c
        n = n + 1
        if (abs(z) > zlimit):
            return n
    return n


def snapshot (x,y,scale):
    # snapshot centered at x,y and with zoom x(1/scale)
    global npixels, borders, rad

    rad = rad / scale
    xmin = x - rad
    ymin = y - rad

    dx = 2 * rad / (npixels-1)
    dy = dx
    v = []
    for ix in range(npixels):
        for iy in range(npixels):
            x = xmin + dx * ix
            y = ymin + dy * iy
            n = sisosig(x,y)
            v.append(n)
    v = np.reshape (v, (npixels,npixels)).T
    return v


def step(dummy):
    v = snapshot(xtarget,ytarget,scale=2)
    mat.set_data(v)
    return v

mymap = plt.cm.get_cmap('hot')#, 8)    # 8 discrete colors, from 0 to 7.

# set up animation
v = snapshot(xtarget,ytarget,scale=1.)
fig, ax = plt.subplots(figsize=(8,8))
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
mat = ax.imshow(v, cmap=mymap)
# Uncomment the next line to create an animation that zooms in:
#anim = animation.FuncAnimation(fig, step)#, frames=gen, interval=1, repeat=False)#, blit=True)#, repeat = False)
plt.show()

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
