filenames = [
    # '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/dogs.txt',
    '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/cats.txt',
    'cats.txt'
]
for filename in filenames:

    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:

        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)
