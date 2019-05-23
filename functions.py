def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print('Start')
greet_user("Julian", "Montejano")
# when a defined function has a parameter, it must be filled for the function to work
greet_user("Rachel", "Douglas")
greet_user(last_name="Montejano", first_name="Nicholas")
# in this case keyword arguments can be used to improved the readability of the code, but every argument must be named
# best practice is for sharing with others
print('Finish')