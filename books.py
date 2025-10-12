# CSU Global Bookstore Points Program (with ranges)

# Ask the user for the number of books purchased this month
books = int(input("Enter the number of books purchased this month: "))

# Determine the number of points awarded based on ranges
if books <= 0:
    points = 0
elif books <= 3:
    points = 5
elif books <= 5:
    points = 15
elif books <= 7:
    points = 30
else:  # 8 or more
    points = 60

# Display the result
print(f"You have earned {points} points this month.")
