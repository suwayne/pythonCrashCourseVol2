filename = '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/konwledgeGained.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents.replace('python', 'programming'))
