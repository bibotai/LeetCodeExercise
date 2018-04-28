"""
问题链接：
https://www.lintcode.com/en/problem/partition-array/

问题描述：
数组划分
给出一个整数数组 nums 和一个整数 k。划分数组（即移动数组 nums 中的元素），使得：

所有小于k的元素移到左边
所有大于等于k的元素移到右边
返回数组划分的位置，即数组中第一个位置 i，满足 nums[i] 大于等于 k。

 注意事项
你应该真正的划分数组 nums，而不仅仅只是计算比 k 小的整数数，如果数组 nums 中的所有元素都比 k 小，则返回 nums.length。

样例
给出数组 nums = [3,2,2,1] 和 k = 2，返回 1.

"""

#思路：
#给数组nums排序，返回>=k的下标；如果都比k小，则返回nums.length


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        nums = sorted(nums)
        result = len(nums)
        for i in range(len(nums)):
            if(nums[i] >= k):
                result = i
                break
        return result

#测试用例
if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 2]
    k = 2
    print(solution.partitionArray(nums,k))


    nums = [1, 2, 3, 2]
    k = 4
    print(solution.partitionArray(nums,k))


    nums = []
    k = 4
    print(solution.partitionArray(nums,k))