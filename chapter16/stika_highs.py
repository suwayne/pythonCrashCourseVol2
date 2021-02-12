import csv
import matplotlib.pyplot as plt

# filename = '/Users/wayne/Documents/dev/pythonCrashCourseVol2/chapter16/data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)

#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
        
filename = '/Users/wayne/Documents/dev/pythonCrashCourseVol2/chapter16/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# print(highs)

#plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

#format plot
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temparature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

