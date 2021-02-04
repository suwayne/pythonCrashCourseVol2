import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth =1)

#set chart title and label axes.
ax.set_title("Square Numbers", fontsize=7)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=7)

#size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
