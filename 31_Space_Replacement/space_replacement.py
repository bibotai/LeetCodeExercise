# coding:utf-8
"""
问题链接：
https://www.lintcode.com/en/problem/space-replacement/

问题描述：
设计一种方法，将一个字符串中的所有空格替换成 %20 。你可以假设该字符串有足够的空间来加入新的字符，且你得到的是“真实的”字符长度。

你的程序还需要返回被替换后的字符串的长度。

Example:

对于字符串"Mr John Smith", 长度为 13

替换空格之后，参数中的字符串需要变为"Mr%20John%20Smith"，并且把新长度 17 作为结果返回。

思路：
因为使用“%20”替换空格 所以之前一个字符变成了三个字符，
只要每个空格字符乘2再加上原有长度就是新长度。
然后对字符进行双指针遍历。如果不是空格，双指针各减1，如果是空格，倒序替换字符，并且新长度指针-3 旧长度指针-1
"""

class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        # write your code here
        if length == 0:  
            return 0  
        blankCount = 0  
        for i in string:  
            if i == ' ':  
                blankCount += 1  
        new_length = length + blankCount * 2  
       
        leftindex = length - 1  
        rightindex = new_length - 1  
        while leftindex >= 0:  
            if string[leftindex] != ' ':  
                print rightindex,leftindex
                string[rightindex] = string[leftindex]  
                rightindex -= 1  
                leftindex -= 1  
            else:  
                string[rightindex] = '0'  
                string[rightindex - 1] = '2'  
                string[rightindex - 2] = '%'  
                rightindex -= 3  
                leftindex -= 1  
        return new_length  

# print Solution().replaceBlank(['M','r',' ','J','o','h','n',' ','S','m','i','t','h'],13)

print Solution().replaceBlank('Mr John Smith',13)