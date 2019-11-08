#### 条件分支 ####
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

### if usage with list ###
lis0 = [value * 2 for value in range(2, 6)]
print(lis0)

# in/not in
if 14 in lis0:
    print('yes')
elif 9 not in lis0:
    print('9 not in')
# check list not empty
lis1 = []
if lis1:
    print("list is not empty.")
else:
    print("list is empty.")
# check list in another list
lis3 = ["peppers", "olives", "apple"]
lis4 = ["peppers", "olives", "mushrooms"]
for li in lis3:
    if li in lis4:
        print(li + " in another list")
    else:
        print(li + " not in anther list")

