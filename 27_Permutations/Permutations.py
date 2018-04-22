"""
问题链接：
http://www.lintcode.com/zh-cn/problem/permutations/

问题描述：
全排列
给定一个数字列表，返回其所有可能的排列。

例如：
给出一个列表[1,2,3]，其全排列为：

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

#思路：
# 两种解决办法
# 1.python itertools
# 2.递归实现，一次选一个数字出来，其他数字重新组合。
import itertools
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute_1(self,nums):
        return list(itertools.permutations(nums))

    def permute_2(self, nums):
        # write your code here
        if(len(nums)<2):
            return [nums]
        result=[]
        for i in range(len(nums)):
            p = self.permute_2(nums[:i]+nums[i+1:])
            for x in p:
                result.append(nums[i:i+1]+x)
        return result

#测试用例
if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute_1(nums))
    print(solution.permute_2(nums))

    nums = [1]
    print(solution.permute_1(nums))
    print(solution.permute_2(nums))

    nums = [1, 4, 7]
    print(solution.permute_1(nums))
    print(solution.permute_2(nums))
