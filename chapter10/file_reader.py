# file_path = '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter9/pi_digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()

# print(contents)

filename = '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter9/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
