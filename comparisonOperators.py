temperature = 35

if temperature > 30:
    print("it's a hot day")
else:
    print("it's not a hot day")

name = 'Julian'
print(len(name))

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a max of 50 characters")
else:
    print("Name is alright")

# we can do comparisons with the equals sign like js
# == equal
# != not equal

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")