filenames = [
    '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/dogs.txt',
    '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/cats.txt',
]
for filename in filenames:
    print(f"\nReading file: {filename}")

    try:  # run the code below

        with open(filename) as f:
            contents = f.read()
            print(contents)

    except FileNotFoundError:  # execute this code when there is an exception
        print("Sorry, I cant find the file.")
