# coding:utf-8
"""
问题链接：
https://leetcode.com/problems/single-number/description/

问题描述：
给你一个数组，数组里面的数字都是成对出现的，只有一个不是成对出现的，找个那个单身狗
Example:
Input: [1,2,1,3,4,2,3]
Output: 4
思路：
创建一个数组，去一个数出来，与新数组里面的数进行对比，有的话删除新数组里面相同的数，没有的话加入到新数组中
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()
if __name__ == '__main__':
    a = [1,2,1,3,4,2,3]
    print singleNumber(a)