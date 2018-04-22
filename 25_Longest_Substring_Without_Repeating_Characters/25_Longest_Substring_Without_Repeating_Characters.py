# coding:utf-8
"""
问题链接：
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

问题描述：
找出一个字符串中，连续的，且不包含重复字符的，最长的字符串的长度
Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
思路：
开辟一个数组，存放字符和字符的位置，然后遍历字符串中的所有字符。
如果字符不在新数组中，将这个字符和位置加入数组
如果字符在新的数组中，长度从这个字符的上一个位置开始计算。
长度的计算为从当前位置到上一个重复字符的位置，并记录下，留着做比较

"""
def lengthOfLongestSubstring(s):
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1#开始的位置
        else:
            maxLength = max(maxLength, i - start + 1)#计算最大的长度
        usedChar[s[i]] = i

    return maxLength
if __name__ == '__main__':
    a = "abcbcdefgg"
    print lengthOfLongestSubstring(a)