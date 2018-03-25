"""
问题链接：
https://leetcode.com/problems/reverse-string/description/

问题描述：
编写一个函数，该函数以字符串作为输入，并返回翻转后的字符串。

例子:
Given s = "hello", return "olleh".
"""
from collections import deque


class Solution:
    #Python翻转字符串(reverse string), 一共包含5种方法 , 如下:
    #1. 简单的步长为-1, 即字符串的翻转(常用);
    #时间复杂度 O(1)
    #空间复杂度 O(1)
    def reverseString_1(self, s):
        return s[::-1]
    #2. 交换前后字母的位置;
    #时间复杂度 O(n)
    #空间复杂度 O(1)
    def reverseString_2(self, s):
        t = list(s)
        l = len(t)
        for i,j in zip(range(l-1, 0, -1), range(l//2)):
            t[i], t[j] = t[j], t[i]
        return "".join(t)
    #3. 递归的方式, 每次输出一个字符;
    #时间复杂度 O(n)
    #空间复杂度 O(n)
    def reverseString_3(self, s):
        if len(s) <= 1:
            return s
        return self.reverseString_3(s[1:]) + s[0]
    #4. 双端队列, 使用extendleft()函数;
    #时间复杂度 O(n)
    #空间复杂度 O(n)
    def reverseString_4(self, s):
        d = deque()
        d.extendleft(s)
        return ''.join(d)
    #5. 使用for循环, 从左至右输出;
    #时间复杂度 O(n)
    #空间复杂度 O(1)
    def reverseString_5(self, s):
        return ''.join(s[i] for i in range(len(s) - 1, -1, -1))

#测试用例
if __name__ == '__main__':
    reserve = Solution()
    s = "hello"
    # example :
    print(reserve.reverseString_1(s))
    print(reserve.reverseString_2(s))
    print(reserve.reverseString_3(s))
    print(reserve.reverseString_4(s))
    print(reserve.reverseString_5(s))


    s = "kfsf234012"
    #其他字符串:
    print(reserve.reverseString_1(s))
    print(reserve.reverseString_2(s))
    print(reserve.reverseString_3(s))
    print(reserve.reverseString_4(s))
    print(reserve.reverseString_5(s))