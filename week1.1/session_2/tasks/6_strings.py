# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")
print(f"\nOriginal String: {user_string}")

#将所有字母转化为小写
print(f"Modified String 1: {user_string.lower()}")

# 将字符串中的所有字母转换为大写
print(f"Modified String 2: {user_string.upper()}")

# 删除字符串首尾的空格
print(f"Modified String 3: {user_string.strip()}")

# 将字符串中的字母 a 替换为 @
print(f"Modified String 4: {user_string.replace('a', '@')}")

# 将字符串首字母大写，其余字母小写
print(f"Modified String 5: {user_string.capitalize()}")

# 反转字符串
print(f"Modified String 6: {user_string[::-1]}")

# 将每个单词的首字母转换为大写
print(f"Modified String 7: {user_string.title()}")

# 计算字符串的字符总数
print(f"Modified String 8: {len(user_string)}")

# 查找字母 a 第一次出现的位置
print(f"Modified String 9: {user_string.find('a')}")

# 统计字母 a 在字符串中出现的次数
print(f"Modified String 10: {user_string.count('a')}")

# 检查字符串是否以 Hello 开头
print(f"Modified String 11: {user_string.startswith('Hello')}")

# 检查字符串是否以感叹号结尾
print(f"Modified String 12: {user_string.endswith('!')}")

# 检查字符串是否只包含字母和数字
print(f"Modified String 13: {user_string.isalnum()}")

# 检查字符串是否只包含字母
print(f"Modified String 14: {user_string.isalpha()}")

# 检查字符串是否只包含数字
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!