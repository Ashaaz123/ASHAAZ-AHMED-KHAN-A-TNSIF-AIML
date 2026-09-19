arr1 = [1, 2, 2, 3, 4]
arr2 = [4, 2, 1, 2, 3]

if len(arr1) != len(arr2):
    print("Arrays are Not Equal")
else:
    equal = True

    for num in arr1:
        if arr1.count(num) != arr2.count(num):
            equal = False
            break

    if equal:
        print("Arrays are Equal")
    else:
        print("Arrays are Not Equal")