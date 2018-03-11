#coding=utf-8

"""
问题链接：
https://leetcode.com/problems/longest-common-prefix/description/
PS：参考了一下别人的算法
问题描述：
给一堆字符串，这额字符串都有一个公共的前缀，需要输出这个前缀

例：
输入：
    ICMP123
    ICMP134
    ICMP99

输出：
    ICMP

"""

"""
思路1：
得把每个字符串的第i 个字符拿出来比较一下（从0开始），一样的话再读取下一个，不一样的话，前面的就是最长的前缀

调用两个python内置函数
    zip：zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    >>>a = [1,2,3]
    >>> b = [4,5,6]
    >>> c = [4,5,6,7,8]
    >>> zipped = zip(a,b)     # 打包为元组的列表
    [(1, 4), (2, 5), (3, 6)]
    >>> zip(a,c)              # 元素个数与最短的列表一致。
    [(1, 4), (2, 5), (3, 6)]

接下来就简单了，将元组中多余的元素剔除（或者说统计不同元素的个数）
    set 就可以直接用
        >>>x = set('runoob')
        set(['b', 'r', 'u', 'o', 'n']
        看出来，o就剩i 个了
        接下来判断一下长度就可以了
"""



def longestCommonPrefix(list):
    for i, j in enumerate(zip(*list)):
        print j
        print set(j)
        if len(set(j)) != 1:#不一样的时候，一样的时候=1
            print list[0][:i]
            break

#测试用例
if __name__ == '__main__':
    list1 = ["ICMP1234abcdjkafnjk", "ICMP1234abcasmvmwor", "ICMP1234abcvmieor", "ICMP1234abcfdsgdfggdfgerg"]
    longestCommonPrefix(list1)
"""
调试结果
('I', 'I', 'I', 'I')
set(['I'])
('C', 'C', 'C', 'C')
set(['C'])
('M', 'M', 'M', 'M')
set(['M'])
('P', 'P', 'P', 'P')
set(['P'])
('1', '1', '1', '1')
set(['1'])
('2', '2', '2', '2')
set(['2'])
('3', '3', '3', '3')
set(['3'])
('4', '4', '4', '4')
set(['4'])
('a', 'a', 'a', 'a')
set(['a'])
('b', 'b', 'b', 'b')
set(['b'])
('c', 'c', 'c', 'c')
set(['c'])
('d', 'a', 'v', 'f')
set(['a', 'f', 'd', 'v'])
ICMP1234abc
"""