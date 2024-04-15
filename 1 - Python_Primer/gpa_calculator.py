"""
The following is python program that computes a grade-point average (GPA)
"""

# The following print prompt can also be written in single print using triple-quoted string
print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')

points = { "A+" :4.0,  "A" :4.0, "A-" :3.67, 
           "B+" :3.33, "B" :3.0, "B-" :2.67,
           "C+" :2.33, "C" :2.0, "C"  :1.67, 
           "D+" :1.33, "D" :1.0, "F"  :0.0 }

nums_courses = 0
total_points = 0
done = False

while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Unknown grade '{0}' being ignored".format(grade))
    else:
        nums_courses += 1
        total_points += points[grade]

if nums_courses > 0:
    print('You GPA is {0: .3}'.format(total_points/ nums_courses))
    
    

def compute_gpa(grades, points = points):
    nums_courses = 0
    total_points = 0
    for g in grades: 
        if g in points:
            nums_courses += 1
            total_points += points[g]
    return total_points/nums_courses
    
    