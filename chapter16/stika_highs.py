import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '/Users/wayne/Documents/dev/pythonCrashCourseVol2/chapter16/data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#get dates and high temparatures from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

#plot the high temparatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#format plot
plt.title("Daily high temparatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temparature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()














