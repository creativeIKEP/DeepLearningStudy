import math
import numpy as np
from matplotlib import pyplot

x = np.arange(0, 6, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

pyplot.plot(x, y_sin, label="sin")
pyplot.plot(x, y_cos, color='red', linestyle='dashed', linewidth = 1.0, label="cos")
pyplot.xlabel("x")
pyplot.ylabel("y")
pyplot.title("sin & cos")
pyplot.legend()
pyplot.show()
