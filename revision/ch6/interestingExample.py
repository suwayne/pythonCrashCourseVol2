alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'   #added this part, because I was paying too much attention to the book.
#move the alien to the right
#determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3

#the new position is the old position + the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"new position: {alien_0['x_position']}")

