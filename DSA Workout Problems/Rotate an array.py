arr = [1, 2, 3, 4, 5]
k = 2

n = len(arr)

k = k % n

for i in range(k):
    last = arr[-1]

    for j in range(n - 1, 0, -1):
        arr[j] = arr[j - 1]

    arr[0] = last

print(arr)