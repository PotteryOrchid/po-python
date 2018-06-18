# for list
magicians = ['alice','david','carolina']
for mgc in magicians:
	print(mgc)
print('For is over !!')

# range(1,4): 1 <= value < 4
for v in range(1,4):
	print(v)

# Create list by range.
lst1 = list(range(1,10,2))
print(lst1)

lst2 = []
for x in range(1,5):
	lst2.append(x)
print(lst2)

print(min(lst2))
print(max(lst2))
print(sum(lst2))

# 通过 range 创建列表
lst3 = [value**2 for value in range(1,4)]
print(lst3)