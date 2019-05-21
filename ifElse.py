is_hot = False
is_cold = False
# setting a boolean

if is_hot:
    # only runs of the condition is true
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    # works like else if
    print("It's a cool day")
    print("Wear warm clothes")
else:
    # happens only of both statements are false
    print("It's a lovely day")
print("Enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Your down payment is: ${down_payment}")
# formatted string will work better for this type of statement
