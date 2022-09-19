# filename = '/Users/osasu/Documents/dev/pythonCrashCourseVol2/revision/ch10/pi_digits.txt'

# with open(filename) as file_object:
#     contents = file_object.read()
# print(contents)                 

# #or 

# with open('ch10/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)   

filename = 'ch10/pi_digits.txt'
with open(filename) as file_object: 
    for line in file_object:
        print(line.strip())

