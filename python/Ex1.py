marks = [78, 45, 92, 33, 67, 88]
passed = 0

for mark in marks:
    if mark >= 40:
        print(mark, "pass")
        passed += 1
    else:
        print (mark, "fail")
        print("passed:", passed)