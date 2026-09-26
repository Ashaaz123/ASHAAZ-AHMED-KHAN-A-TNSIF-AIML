import numpy as np

marks = np.array([65, 82, 74, 91, 56, 88, 72, 95, 68, 79])

print("Marks:", marks)

print("Total marks:", np.sum(marks))
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))

print("Marks greater than 75:", marks[marks > 75])