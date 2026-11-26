students = [
{"name": "Ali",   "marks": [80, 75, 90]},
{"name": "Sara",  "marks": [95, 88, 92]},
{"name": "Ahmed", "marks": [55, 62, 48]},
]
topper = ""
highest_avg = 0

for student in students:
    name = student["name"]
    marks = student["marks"]

    avg = sum(marks) / len(marks)

    if avg >= 60:
        result = "Pass"
    else:
        result = "Fail"

    print(name, round(avg, 2), result)

    if avg > highest_avg:
        highest_avg = avg
        topper = name

print("Topper:", topper)