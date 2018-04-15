# coding:utf-8
"""
问题链接：
https://leetcode.com/problems/search-for-a-range/description/

问题描述：
给定按升序排序的整数num数组，找到给定目标值的起始和结束位置。

算法的运行时复杂度必须按照O（log n）的顺序。

如果在数组中找不到目标，则返回[-1，-1]。
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
思路：
二分法速度最快，找到最左边的值+1，最右边的值-1
"""


def extreme_insertion_index(self, nums, target, left):
    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target or (left and target == nums[mid]):
            hi = mid
        else:
            lo = mid + 1

    return lo


def searchRange(self, nums, target):
    left_idx = self.extreme_insertion_index(nums, target, True)

    # assert that `left_idx` is within the array bounds and that `target`
    # is actually in `nums`.
    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]

    return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]

