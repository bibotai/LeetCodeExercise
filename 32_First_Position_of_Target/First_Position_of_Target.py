"""
问题链接：
https://www.lintcode.com/en/old/problem/first-position-of-target/

问题描述：
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。

您在真实的面试中是否遇到过这个题？
样例
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。

"""

#思路：
#二分查找也即折半查找，是一种效率较高的查找方法
#给定下标为中间位置，判断中间位置的值与目标值的大小，然后更改low或者high的位置
#因返回的是第一次出现下标的位置，所以不仅需要判断中间位置的值是否与目标值大小相等 还需要判断其前一位的值是不是也与目标值大小相等

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target and nums[mid-1] != target:
                return mid
            elif nums[mid] > target or nums[mid-1] == target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
#测试用例
if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 3, 4, 5, 10]
    target = 3
    print(solution.binarySearch(nums,target))


    nums = [1, 3, 3, 3, 4, 5, 5, 10]
    target = 5
    print(solution.binarySearch(nums,target))
