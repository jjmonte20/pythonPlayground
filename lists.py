names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[-1])
# negative values always go to the end of the list
print(names[2:])
# : can make an index that will go from the 3rd position to the end
print(names[2:4])
# going to a number will return between position 2 and 4, but not 4 itself
numbers = [3,5,2,4,1,8]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(max)