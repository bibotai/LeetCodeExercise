"""
问题链接：
https://leetcode.com/problems/valid-palindrome/description/

问题描述：
给定一个字符串，确定它是否是回文，只考虑字母数字字符和忽略大小写。

例如：
"A man, a plan, a canal: Panama" 是回文字符串。
"race a car" 不是回文字符串。

注意:
你有考虑过这个字符串可能是空的吗？ 在面试中这是一个很好的问题。
针对此题目，我们将空字符串定义为有效的回文字符串。
"""

from collections import deque
import re
class Solution:
    #对于一个字符串 如果它是轴对称的 即为回文字符串

    #上一周 11_Reverse_String 翻转字符串 除了递归均可以用这个方法 如下，共四种：
    #1. 简单的步长为-1, 即字符串的翻转(常用);
    #时间复杂度 O(1)
    #空间复杂度 O(1)
    def isPalindrome_1(self, s):
        s = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）:：]+", "", s.lower())
        if len(s)==0:
            return True
        else:
            return s==s[::-1]
    #2. 交换前后字母的位置;
    #时间复杂度 O(n)
    #空间复杂度 O(1)
    def isPalindrome_2(self, s):
        s = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）:：]+", "", s.lower())
        if len(s) == 0:
            return True
        else:
            t = list(s)
            l = len(t)
            for i,j in zip(range(l-1, 0, -1), range(l//2)):
                t[i], t[j] = t[j], t[i]
            return s == "".join(t)
    #3. 双端队列, 使用extendleft()函数;
    #时间复杂度 O(n)
    #空间复杂度 O(n)
    def isPalindrome_3(self, s):
        s = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）:：]+", "", s.lower())
        if len(s) == 0:
            return True
        else:
            d = deque()
            d.extendleft(s)
            return s == ''.join(d)
    #4. 使用for循环, 从左至右输出;
    #时间复杂度 O(n)
    #空间复杂度 O(1)
    def isPalindrome_4(self, s):
        s = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）:：]+", "", s.lower())
        if len(s) == 0:
            return True
        else:
            return s == ''.join(s[i] for i in range(len(s) - 1, -1, -1))

    # 5. 使用循环 对给定字符串 分别用一个指针（本例中使用字符串下标）指向字符串的头尾字符
    # 每次将指针向中间字符靠拢，循环迭代，出现不相等的情况即可跳出循环，返回false，若循环一直到结束，则返回true。
    # 时间复杂度 O(n/2)
    # 空间复杂度 O(1)
    def isPalindrome_5(self, s):
        s = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）:：]+", "", s.lower())
        if len(s) == 0:
            return True
        else:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            return True

#测试用例
if __name__ == '__main__':
    palindrome = Solution()
    s = "A man, a plan, a canal: Panama"
    # example :
    print(palindrome.isPalindrome_1(s))
    print(palindrome.isPalindrome_2(s))
    print(palindrome.isPalindrome_3(s))
    print(palindrome.isPalindrome_4(s))
    print(palindrome.isPalindrome_5(s))

    s = "race a car"
    # example :
    print(palindrome.isPalindrome_1(s))
    print(palindrome.isPalindrome_2(s))
    print(palindrome.isPalindrome_3(s))
    print(palindrome.isPalindrome_4(s))
    print(palindrome.isPalindrome_5(s))

    s = ""
    # example :
    print(palindrome.isPalindrome_1(s))
    print(palindrome.isPalindrome_2(s))
    print(palindrome.isPalindrome_3(s))
    print(palindrome.isPalindrome_4(s))
    print(palindrome.isPalindrome_5(s))


