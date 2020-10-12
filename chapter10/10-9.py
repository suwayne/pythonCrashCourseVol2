import os
import sys
# changing the working directory
os.chdir('/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/')
# adding to your python path
sys.path.append(
    '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/')

filenames = [
    # '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/dogs.txt',
    '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/cats.txt',
    'cats.txt',
    'zombie.txt',
]
for filename in filenames:

    try:  # run the code below
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:  # execute the code below when there is an exception

        pass

    else:
        print(f"\nReading file: {filename}")
        print(contents)
