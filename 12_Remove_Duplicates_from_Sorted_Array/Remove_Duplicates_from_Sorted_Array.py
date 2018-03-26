# coding:utf-8
"""
问题链接：
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

问题描述：
对一个数组中不同的元素进行计数，并返回长度。

Example:
Input: nums = [1,1,2]
Output: length = 2

问题思路：
问题本身不难，编译一遍，去除挨着的重复的数就行，但如果数据不是从小到大排列，则需要先进行一下排序比较好。
另外，不能创建新的数组
"""


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i = i+1
            nums[i] = nums[j]
    return i + 1
if __name__ == '__main__':
    abc = [1,6,9,4,5,7,11,57,33,22,11,85,3,1,5]
    bcd = removeDuplicates(abc)
    print bcd