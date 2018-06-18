#### Base knowledge: print ####
print("Hello python world! \n")

msg = "Hello world by msg"
print(msg)

# 制表符：\t 换行：\n 换行：\r \f \b \a \v
print("tab:\t==new_line:\r==FF:\f==BS:\b==BEL:\a==VT:\v==new_line:\n==")



#### String ####
str0 = "coding Man"

# 首字母大写转换
print("First word upper: " + str0.title())
# 大写转换
print("All word upper: " + str0.upper())
# 小写转换
print("All word lower: " + str0.lower())
str1 = " is Me"
print(str0 + str1)

# 去除空白符
str2 = " hello "
print("==" + str2.rstrip() + "==")
print("==" + str2.lstrip() + "==")
print("==" + str2.strip() + "==")



#### Integer ####
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(3 / 2)



#### Float ####
# result = 0.30000000000000004
print(0.2 + 0.1)
print(0.2 + 0.2)


#### 类型转换 ####
# str()
print("I am " + str(20) + " years old.")

