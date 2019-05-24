import random

members = ['John', 'Julian', 'Rachel', 'Mosh']

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))
    leader = random.choice(members)
    print(leader)