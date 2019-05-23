try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
    # best practice will always be to make code to handle many different user input situations
except ValueError:
    # will only catch error for different data types
    print('Invalid value, please use a digit like 1 2 3 4 5 6 7 8 9 0')
    # using an exception will allow the code to successfully finish without crashing
# exit code 0 means everything went well
# exit code 1 means there is a problem with the code that caused a crash
