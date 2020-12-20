#plotting the first 5 cubic numbers
import matplotlib.pyplot as plt
x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

#set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()
plt.savefig('cubes_plot.png', bbox_inches='tight')

