# Write a Python program to calculate an electricity bill based on the number of units consumed by a user.

# Requirements:
# 1. Take electricity units as input from the user.
# 2. If units are negative, display Invalid Units.
# 3. Calculate the bill using the following progressive slab rates:
# Electricity Units	Rate
# First 100 units	₹5 per unit
# Next 100 units	₹7 per unit
# Next 100 units	₹10 per unit
# Above 300 units	₹12 per unit





unit = int(input("Enter your units: "))

if unit < 0:
    print("Invalid units")

elif unit <= 100:
    bill = unit * 5

elif unit <= 200:
    bill = (100 * 5) + (unit - 100) * 7

elif unit <= 300:
    bill = (100 * 5) + (100 * 7) + (unit - 200) * 10

else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + (unit - 300) * 12

if unit >= 0:
    if bill > 2000:
        bill = bill + (bill * 5 / 100)

    print(f"Your electricity bill is: ₹{bill:.2f}")

