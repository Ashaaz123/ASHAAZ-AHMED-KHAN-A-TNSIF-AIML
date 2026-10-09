arr = [100, 4, 200, 1, 3, 2]

numbers = set(arr)

max_length = 0

for num in numbers:

    if num - 1 not in numbers:

        current = num
        length = 1

        while current + 1 in numbers:
            current += 1
            length += 1

        if length > max_length:
            max_length = length

print("Longest Consecutive Sequence:", max_length)