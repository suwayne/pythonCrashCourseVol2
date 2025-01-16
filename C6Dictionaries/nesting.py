# alien_0 = {'color': 'green', 'points': 5, }
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# for value in range(1, 5):
#     print(value)

# empty list storing aliens
aliens = []
# make 30 aliens
for alien_number in range(30):
    alien = {'color': 'green', 'speed': 'slow', 'points': 5, }
    aliens.append(alien)

# show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)

# show how many aliens have been created.
print("total number of aliens: " + str(len(aliens)))
print("...")

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
