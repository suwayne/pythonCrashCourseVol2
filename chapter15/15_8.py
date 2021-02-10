from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create two D6 dice.
die_1 = Die(8)
die_2 = Die(8)

#make some rolls and store the result in a list
results = []
for rull_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#analyze results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two dice of 8 sides a thousand times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
