import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June"]
sales = [12000, 15000, 13000, 18000, 20000, 22000]

# Line Chart
plt.plot(months, sales, marker="o", label="Sales")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.legend()

plt.show()


# Bar Chart
plt.bar(months, sales, label="Sales")

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.legend()

plt.show()