# import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]

# fig, ax = plt.subplots()
# ax.plot(squares)

# plt.show()

# import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]

# fig, ax = plt.subplots()
# ax.plot(squares, linewidth=3)

import numpy as np
import matplotlib.pyplot as plt

x = np.arrange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
