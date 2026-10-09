arr = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(arr)):
    required = target - arr[i]

    if required in seen:
        print([seen[required], i])
        break

    seen[arr[i]] = i