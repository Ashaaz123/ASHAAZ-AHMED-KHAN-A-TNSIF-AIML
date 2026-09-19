arr = [2, 5, 2, 8, 5, 2, 3, 5, 2]

max_frequency = 0
most_frequent = arr[0]

for num in arr:
    count = 0

    for x in arr:
        if x == num:
            count += 1

    if count > max_frequency:
        max_frequency = count
        most_frequent = num

print("Most Frequent Element:", most_frequent)
print("Frequency:", max_frequency)