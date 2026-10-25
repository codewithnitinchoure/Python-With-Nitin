pin = int(input("enter your pin :"))

if pin == 5445:
    print("login Successful....")

    balance = 5000

    askuser = int(input("how much money they want to withdraw "))

    if askuser > 5000:
        print(f"insufficient balance, your balance is {balance}, you not ebale withdraw:{askuser}")

       

    elif askuser <= balance:
        x = balance - askuser
        print(f"successful withdraw and remaining balance is {x}")


else:
    print("incorret pin , enter correct pin ")