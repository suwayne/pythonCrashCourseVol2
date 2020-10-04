filename = '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/longer_pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()

# print(pi_string)
# print(len(pi_string))


for line in lines:
    pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

# working with pi having more digital places and displaying the first 52 characters.
print(f"{pi_string[:52]}...")
print(f" The length of the string is: {len(pi_string)}")
