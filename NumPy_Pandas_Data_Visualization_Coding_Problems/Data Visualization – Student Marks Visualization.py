import matplotlib.pyplot as plt

students = ["Asha", "Rahul", "Priya", "Arun", "Divya",
            "Karan", "Meena", "Vijay", "Ravi", "Sneha"]

marks = [85, 72, 91, 68, 55, 88, 35, 95, 45, 78]

# Bar Chart
plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.xticks(rotation=45)

plt.show()


# Performance Categories
excellent = 0
good = 0
average = 0
needs_improvement = 0

for mark in marks:
    if mark >= 80:
        excellent += 1
    elif mark >= 60:
        good += 1
    elif mark >= 40:
        average += 1
    else:
        needs_improvement += 1

categories = ["Excellent", "Good", "Average", "Needs Improvement"]
values = [excellent, good, average, needs_improvement]

# Pie Chart
plt.pie(values, labels=categories, autopct="%1.1f%%")

plt.title("Student Performance Distribution")

plt.show()