# for list
magicians = ['alice', 'david', 'carolina']

for mgc in magicians:
    print(mgc)
print('For is over !!')
print(magicians[0])

# range(1,4): 1 <= value < 4
for v in range(1, 4):
    print(v)

# Create list by range.
lst1 = list(range(1, 10, 2))
print("lst1: " + str(lst1))

lst2 = []
for x in range(1, 5):
    lst2.append(x)
print(lst2)

print(min(lst2))
print(max(lst2))
print(sum(lst2))

# 通过列表解析 range 创建1-5的平方数列表
lst3 = [value ** 2 for value in range(1, 6)]
print("列表解析" + str(lst3))

# 获取部分列表值 start <= n < last
print(lst3[0:2])
# 从头开始
print(lst3[:2])
# 从某一位置到结尾
print(lst3[3:])
# 获取后几位
print("last two number: " + str(lst3[-2:]))
# 获取倒数第几位
print("the third number from the end: " + str(lst3[-3]))

# Copy list
lst4 = lst3[:]
print(lst4)

print("======test======")

'''print 1-20 by for key word.'''
for val in range(1, 21):
    print(val, end=' ')
