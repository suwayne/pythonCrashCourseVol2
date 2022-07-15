#make an empty list for storing aliens

aliens = []

#make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

"""
#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
"""

#here, you're going to change the first 3 aliens to the color yellow, medium-speed, worth 10 points each.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
        aliens.append(alien)


#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)


