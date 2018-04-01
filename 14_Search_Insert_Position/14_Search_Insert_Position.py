# coding:utf-8
"""
问题链接：
https://leetcode.com/problems/search-insert-position/description/

问题描述：
给你一个数组，再给一个数字。找出这个数字在这个数组中的位置；如果没有这个数，找到这个数插入数组的位置
Example 1:
Input: [1,3,5,6], 5
Output: 2
Example 2:
Input: [1,3,5,6], 2
Output: 1
Example 3:
Input: [1,3,5,6], 7
Output: 4
Example 1:
Input: [1,3,5,6], 0
Output: 0
思路：
我觉得最好的解决办法是二分法查找。二分法是个通用的方法，好好理解一下。
"""


def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
if __name__ == '__main__':
    a = [1,4,6,7,8,11,12,24,67]
    b = 13
    print searchInsert(a,b)