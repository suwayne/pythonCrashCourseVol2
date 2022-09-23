import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
#subplot() generates one or more plots in the same figure
#fig represents the collection  of plts generated
#ax represents the single plt in the figure
fig, ax = plt.subplots() 
ax.plot(squares, linewidth=1)

#set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
