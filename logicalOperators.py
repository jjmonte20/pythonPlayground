has_high_income = False
has_good_credit = False
has_criminal_record = False

if has_high_income and has_good_credit:
    print("You are eligible for a loan")
elif has_high_income:
    print("You need to have better credit to get this loan")
elif has_good_credit:
    print("You need a higher income to get this loan")
elif has_criminal_record:
    print("I need to ask about your criminal record")
else:
    print("You are ineligible for this loan, you need a higher income and better credit")