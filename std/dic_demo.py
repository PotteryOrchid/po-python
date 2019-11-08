"""
dictionary:
    字典，类似于java中的类。
"""

man = {'gender': 'male', 'name': 'joe'}
print(man['gender'])

# add new element
man['age'] = 30
print(man)

# update element
man['name'] = 'jack'
print(man)

# delete element
del man['gender']
print(man)

# traversing
for key, val in man.items():
    print(str(key) + " : " + str(val))

# traversing keys
for k in man.keys():
    print(str(k))

# traversing values
for v in man.values():
    print(str(v))

# traversing keys in order
for k in sorted(man.keys()):
    print(k)

# traversing values in set
for v in set(man.values()):
    print(v)

# dic in list
fruits = []
apple = {'color': 'red', 'size': 'big'}
banana = {'color': 'yellow', 'size': 'big'}
fruits.append(apple)
fruits.append(banana)
print(fruits)

# list in dic
shop = {"meat": "beef", "fruit": fruits}
for v in shop.values():
    print(v)

# dic in dic
man['shop'] = shop
print("man info")
print(man)
