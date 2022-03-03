import os
os.chdir('/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/')

filename = 'lazarus.txt'

try:
    with open(filename, encoding='UTF-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} does not exist.")

else:
    # count the approximate number of times 'the' appears
    words = contents.lower().count('the ')
    print(words)
