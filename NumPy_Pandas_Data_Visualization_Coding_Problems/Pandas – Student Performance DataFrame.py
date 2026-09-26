import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Priya", "Arun", "Divya", "Karan", "Meena", "Vijay"],
    "Department": ["CSE", "IT", "CSE", "AIML", "IT", "CSE", "AIML", "CSE"],
    "Marks": [85, 72, 91, 68, 78, 88, 55, 95],
    "Attendance": [90, 75, 92, 85, 78, 88, 70, 95]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nFirst 5 students:")
print(df.head())

print("\nAverage marks:")
print(df["Marks"].mean())

print("\nStudents who scored more than 75:")
print(df[df["Marks"] > 75])

print("\nStudents whose attendance is below 80%:")
print(df[df["Attendance"] < 80])

print("\nStudents sorted based on marks:")
print(df.sort_values("Marks"))