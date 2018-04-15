"""
问题链接：
http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array/

问题描述：
假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。
你需要找到其中最小的元素。
你可以假设数组中不存在重复的元素。

例如：
给出[4,5,6,7,0,1,2]  返回 0
"""

#思路：从小到大排列的有序旋转数组+无重复元素+寻找最小元素
# 假定最小元素的下标是0，执行for循环,只要发现比首元素小的数就终止循环，返回该数值；如果未发现比首元素小的数就直接返回首元素
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        temp = 0
        for i in range(1,len(nums)):
            if nums[i]<nums[temp]:
                temp = i
                break
        return nums[temp]
#测试用例
if __name__ == '__main__':
    solution = Solution()
    # example : 给出[4,5,6,7,0,1,2]  返回 0
    print(solution.findMin([4,5,6,7,0,1,2]))

