import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=700)

# set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value of x", fontsize=14)
ax.set_ylabel("Value of y", fontsize=14)

# set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
