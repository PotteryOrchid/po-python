#### 条件分支 ####
lis0 = [value *2 for value in range(2,6)]
print(lis0)

# in/not in
if 14 in lis0:
	print('yes')
elif 9 not in lis0:
	print('9 not in')

# if-elif-else
str0 = "Hello"
if str0.lower() != 'hello':
	print('no')
elif str0 == 'hello':
	print('hello')
else: 
	print('Hello')

# and/or
age0 = 23
age1 = 12
if age0 > 20 and age1 > 17:
	print('yong')
elif age0 > 15 or age1 < 15:
	print('not true')


#### dictionary: 字典，类似于java中的类。 ####
man = {'gener':'male', 'name':'joe'}
print(man['gener'])
man['age'] = 30
print(man['age'])