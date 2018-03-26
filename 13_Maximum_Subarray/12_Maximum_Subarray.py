# coding:utf-8
"""
问题链接：
https://leetcode.com/problems/maximum-subarray/description/

问题描述：
给一个数组，连续几个数相加最大，输出着连续的几个数
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: [4,-1,2,1] has the largest sum = 6.
"""


def maxSubArray(A):
    if not A:
        return 0

    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        print curSum
        maxSum = max(maxSum, curSum)
        print maxSum
        print '\n'
    return maxSum

if __name__ == '__main__':
    a = [-2,1,-3,4,-1,2,1,-5,4]
    b = maxSubArray(a)
    print b
