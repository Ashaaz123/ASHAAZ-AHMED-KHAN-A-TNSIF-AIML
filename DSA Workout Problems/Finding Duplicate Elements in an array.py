# Finding duplicate numbers in an array

arr = [2, 1, 5, 2, 3, 1]

duplicate = -1

for i in range(len(arr)):
  for j in range(i + 1, len(arr)):
    if arr[i] == arr[j]:
      duplicate = arr[i]


  if duplicate !=-1:
    break

print("duplicate element:", duplicate)