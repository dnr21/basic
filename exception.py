try:
    amount = 2999
    if amount < 5999:
        raise ValueError("please add money in  account")
    else:
        print("You are eligible to purchase charger")
except ValueError as e:
        print(e)
