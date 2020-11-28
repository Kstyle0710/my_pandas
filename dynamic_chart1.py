import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 100, 1)

def multi(x):
    return x*2

y = multi(x)
l = plt.plot(x,y)

# ax = plt.axis([0, 100, 0, 1])
#
redDot, = plt.plot([0], [multi(0)], 'ro')

def animate(i):
    redDot.set_data(i, multi(i))
    return redDot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, 100, 0.1), \
                                      interval=0.1, blit=True, repeat=True)

plt.show()