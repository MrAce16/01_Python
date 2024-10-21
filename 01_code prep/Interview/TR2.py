students_grades = {'Alice': {'Math': 85, 'Physics': 90, 'Chemistry': 78, 'cs': 99}, 'Bob': {
    'Math': 92, 'Physics': 88, 'Chemistry': 95}, 'Charlie': {'Math': 87, 'Physics': 85, 'Chemistry': 90}}

avg = 0
sum =0
count=0

for i,v in students_grades.items():
    for j,k in v.items():
        print(j)
        if j == 'Math':
            sum += k 
            count += 1
            avg = sum/count 
            print(avg)
        