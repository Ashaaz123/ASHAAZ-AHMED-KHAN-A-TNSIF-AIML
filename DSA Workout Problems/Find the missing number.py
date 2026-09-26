arr = [1, 2, 3, 5, 6, 7]

n = 7

total = n * (n + 1) // 2

array_sum = 0

for num in arr:
    array_sum += num

missing = total - array_sum

print("Missing Number:", missing)