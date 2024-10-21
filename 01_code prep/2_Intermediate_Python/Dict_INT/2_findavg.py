# You are given a dictionary where the keys are student names and the values are dictionaries representing their grades in various subjects.
# Write a function that takes this dictionary as input and returns a new dictionary where the keys are the subjects and the values are the average grade for each subject.

# Find Avg of Phys, chem and maths
students_grades = {'Alice': {'Math': 85, 'Physics': 90, 'Chemistry': 78, 'cs': 99}, 'Bob': {
    'Math': 92, 'Physics': 88, 'Chemistry': 95}, 'Charlie': {'Math': 87, 'Physics': 85, 'Chemistry': 90}}

avg = 0
d = {}

for i, v in students_grades.items():
    for key, values in v.items():
        if key in d:
            avg += 1
            d[key] += values/avg
        else:
            d[key] = values
print(d)
