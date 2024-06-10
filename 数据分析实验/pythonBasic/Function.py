# 求水仙花数
def find_num(start, end):
    nums = []
    for num in range(start, end):
        if num == sum(int(i) ** 3 for i in str(num)):
            nums.append(num)
    return nums


print(find_num(100, 1000))


# 求阶乘1
def function(n):
    if n == 0:
        return 1
    else:
        return function(n - 1) * n


print(function(5))

# 求阶乘2
n = int(input())
s = 1
for i in range(1, n + 1):
    s = s * i
print(s)

# 求解曲边图形的面积
import math

n = 10000  # 划分的小矩形个数
# 1.将图形等份划分，得到若干小矩形（构建 x 序列）。
width = 2 * math.pi / n  # 每个小矩形的宽度
x = [i * width for i in range(0, n)]  # x 序列
# 2.求出各小矩形的面积。
s = [abs(math.sin(i)) * width for i in x]


#   冒泡排序法
def BubbleSort(nums):
    for i in range(0, len(nums)):
        for j in range(0, len(nums) - i - 1):
            nums[j], nums[j + 1] = nums[j + 1], nums[j]


#   统计词频
from functools import reduce
import re

str1 = ("Youth is not a time of life; it is a state of mind; it is not a matter of rosy cheeks,"
        " red lips and supple knees; it is a matter of the will, a quality of the imagination, "
        "a vigor of the emotions; it is the freshness of the deep springs of life. ")

words = str1.split()  # 以空字符为分隔符对 str1 进行分割
words1 = [re.sub('\W', '', i) for i in words]  # 将字符串中的非单词字符替换为''


def fun(x, y):
    if y in x:
        x[y] = x[y] + 1
    else:
        x[y] = 1
        17
    return x


result = reduce(fun, words1, {})  # 统计词频
print("词频为：", result)


#  求最大公约数
def gcd(num1, num2):
    if num1 > num2:
        small_num = num2
    else:
        small_num = num1
    i, temp = 2, 1
    while i <= small_num:
        if ((num1 % i == 0) and (num2 % i == 0)):
            temp = i
        i += 1
    return temp


# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
print(num1, "和", num2, "的最大公约数为", gcd(num1, num2))
