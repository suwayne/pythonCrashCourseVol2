import matplotlib.pyplot as plt
square = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(square, linewidth=3)
# set chart title and lable axex.

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
