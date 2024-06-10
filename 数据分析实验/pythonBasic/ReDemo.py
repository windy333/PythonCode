# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年12月28日
"""

'''正则表达式示例'''

import re

# 1. 匹配字符串
pattern = r"apple"
text = "I have an apple and a banana"
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

# 2. 搜索和替换
pattern = r"gr[ae]y"
text = "The gray cat is sitting on the grey mat"
replaced_text = re.sub(pattern, "colorful", text)
print("Replaced text:", replaced_text)

# 3. 匹配多个字符
pattern = r"ab+"
text = "This is a test about ab, abb, abbb, and abbbb"
matches = re.findall(pattern, text)
print("Matches:", matches)

# 4. 匹配任意字符
pattern = r"gra.y"
text = "gray, grey, grary, graay"
matches = re.findall(pattern, text)
print("Matches:", matches)

# 5. 匹配重复
pattern = r"(ab){2,3}"
text = "ab, abab, ababab, abababab"
matches = re.findall(pattern, text)
print("Matches:", matches)

# 6. 分组
pattern = r"(\d{3})-(\d{3})-(\d{4})"
text = "Phone numbers: 123-456-7890, 555-666-7777"
matches = re.findall(pattern, text)
for match in matches:
    print("Full match:", match)
    print("Area code:", match[0])
    print("Prefix:", match[1])
    print("Suffix:", match[2])


# 7. 高级功能：使用函数进行替换
def multiply_10(match):
    number = int(match.group(0))
    return str(number * 10)


pattern = r"\d+"
text = "Numbers: 5, 10, 15, 20"
replaced_text = re.sub(pattern, multiply_10, text)
print("Replaced text:", replaced_text)
