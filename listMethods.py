numbers = [5,2,1,7,4]
numbers.append(20)
# append() will insert a number at the end of the list
numbers.insert(0, 10)
# insert() will insert a number a the position passed before the number
numbers.remove(1)
# remove() will remove the number based on what is asked
numbers.pop()
# pop() will remove a number at the end of the list
# numbers.clear()
# clear() will remove all of the items in a list
print(numbers)
print(numbers.index(10))
# be cafeful to make sure index is used before using any mutation methods
numbers.sort()
# sorts the list
print(numbers)
numbers.reverse()
# sorts the list in reverse order
print(numbers)
numbers2 = numbers.copy()
# copy will copy a new list, may be important if lists are immutable
