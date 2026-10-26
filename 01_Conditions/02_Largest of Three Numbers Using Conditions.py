# Write a Python program that takes three numbers as input and prints the largest number using if, elif, and else.
# Input
# 25
# 15
# Output
# Largest number is 25

# code..
A = int(input( "enter the frist number : "  ))
B = int(input( "enter the second number : " ))
C = int(input( "enter the thard number : "  ))


if A >= B and A > C :
    print(f"largest number is :{A} ")

elif B >= A and B > C :
    print(f"largest number is :{B}")

else:
    print(f"largest number is :{C}")