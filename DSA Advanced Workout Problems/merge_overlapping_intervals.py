intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

intervals.sort()

result = []

for interval in intervals:

    if len(result) == 0:
        result.append(interval)

    elif interval[0] <= result[-1][1]:
        result[-1][1] = max(result[-1][1], interval[1])

    else:
        result.append(interval)

print(result)