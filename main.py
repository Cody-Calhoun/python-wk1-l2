# COMPOSITE DATA TYPES

# Tuples
    # Key attributes
        # Immutable (CANNOT CHANGE)
        # Can contain MIXED data types

dog = ('Bruce', 'cocker spaniel', 10, True) 
# print(dog[0])
# This will print Bruce
# dog[3] = False
# This will generate Error

# Lists
    # Key attributes
        # Mutable
        # Can contain MIXED data types
dog2 = ["Garrett", 19, False]
# print(dog2[1])
# This will print 19
# dog2[1] = 10
# print(dog2[1])
# This will print 10

# Slice Operator
    # Allows us to target specific chunks of code
buffalo = [0,7,2,3,4,5,6,7,8,9,10,11,13,56]
# print(buffalo[1:5])
# print(buffalo[1])
# print(buffalo[:4])
# print(buffalo[6:])
# print(int(len(buffalo)/2))
# test = 
# print(buffalo[len(buffalo)//2:])

# Dictionaries
    # Key attributes
        # Key Value Pairs
        # Mutable
        # Can contain MIXED data types

pizza = {
    'style': 'New York', 
    'slices': 8, 
    'size': '8 inches', 
    'ingredients': ['goat cheese', 'bacon', 'green chile'], 
    'delicious': True }
pizza['reorder'] = True
# print(pizza['ingredients'])
# print(pizza[1])
# print(pizza['ingredients'][1])

user = {
    'name': 'Will',
    'age': 29,
    'address': {
        'city':'Jackson Hole',
        'state':'Wyoming'
    }
}

# print(user['address']['city'])

# For Loops

# for x in range(0,10,1):
#     print(x)
# for x in range(7,10):
#     print(x)
# for x in buffalo:
#     print(x)

def add(a,b,repeat=2):	# function name: 'add', parameters: a and b
    x = a + b
    print("Hello world")
    c=8	# process
    return x	# return value: x


add(3,4)