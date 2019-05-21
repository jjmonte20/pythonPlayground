first = 'John'
last = 'Smith'
# John [Smith] is a coder
message = first + " [" + last + "] is a coder"
msg = f'{first} [{last}] is a coder'
print(message)
# concatenated string
print(msg)
# formatted string, this is more optimal for scaling
print(len(msg))
# prints the length of the variable msg
print(msg.upper())
# prints msg in all CAPS
print(msg.lower())
# prints msg in all lowercase