nums = [3, 5, 3, 8, 5, 3, 9]
count = {}
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count [num] = 1
    print(count)