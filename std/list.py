fruits = ['apple', 'banana', 'peach', 'apricot']
print(fruits)
# Get first one
print(fruits[0])
# Get last one
print(fruits[-1])

# Update value
fruits[0] = 'watermelon'
print(fruits)
# Add value
fruits.append('pear')
print(fruits)
# Insert value
fruits.insert(2,'hami melon')
print(fruits)
# Delete value
del fruits[1]
print(fruits)
# pop(): Get and remove value
v1 = fruits.pop()
print(v1)
print(fruits)
v2 = fruits.pop(1)
print(v2)
print(fruits)

# remove(): Remove by value, and only remove one value. (Note: If value is not in list, will return error msg.)
fruits.remove('peach')
print(fruits)

# sort(): Sort value in list.
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# sorted(): Sort values tmp. 临时排序，列表中数据顺序不会改变。
trees = ['willow','maple','poplar']
print(sorted(trees))
print(sorted(trees,reverse=True))
print(trees)

# reverse(): 反转顺序，列表中数据顺序会改变。
trees.reverse()
print(trees)

# len()
print(len(trees))