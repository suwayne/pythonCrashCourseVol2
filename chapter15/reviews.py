# import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# plt.style.use('seaborn-paper')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth =1)

# #set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=7)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=7)

# #size of tick labels.
# ax.tick_params(axis='both', labelsize=14)

# plt.show()

#scatter squares
# import matplotlib.pyplot as plt

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)

# #set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=14)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# #set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

# import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.style.use('seaborn')    
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=20)

# #set chart title and label axes.
# ax.set_title("Square of Numbers", fontsize=12)
# ax.set_xlabel("Value", fontsize=12)
# ax.set_ylabel("Square", fontsize=12)

# #set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=12)

# plt.show()


import matplotlib.pyplot as plt

x_values = (1, 1001)
y_values = (x**2 for x in x_values)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=30)

#set chart title and label axes.
ax.set_title("Square of Numbers", fontsize=12)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square", fontsize=12)

#set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=12)

#set range for each axes
ax.axis([0, 1100, 0, 1100000])

plt.show()
