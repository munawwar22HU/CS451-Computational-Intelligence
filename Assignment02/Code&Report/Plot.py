import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
fig, (ax1,ax2) = plt.subplots(1, 2)
ax1.plot(x,y)
ax1.set_xlabel('x1')
ax1.set_title('Plot')
ax1.set_ylabel('y1')
ax2.plot(x,-y)
ax2.set_xlabel('x2')
ax2.set_title('Plot1')
ax2.set_ylabel('y2')
plt.show()
