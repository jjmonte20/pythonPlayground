customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}
print(customer['name'])
print(customer.get('birthdate', 'Jan 1 1980'))
# similar to objects

customer['name'] = 'Jack Sparrow'
print(customer['name'])