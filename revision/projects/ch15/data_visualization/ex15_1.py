"""
A number raised to the third power is a cube. Plot the first five cubic numbers.
"""
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
output_values = [1, 8, 27, 64, 125]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, output_values, linewidth=1)

#set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

#set size of tick labels.
ax.tick_params(axis="both", labelsize=14)

plt.show()
