"""
问题链接：
https://www.lintcode.com/zh-cn/old/problem/count-1-in-binary/

问题描述：
计算在一个 32 位的整数的二进制表示中有多少个 1.

注意事项
你不可以将物品进行切割。

样例
给定 32 (100000)，返回 1
给定 5 (101)，返回 2
给定 1023 (1111111111)，返回 10
"""

#思路：
#先用bin得到其二进制值
#如果为正数或0，则直接返回二进制里有多少个1
#如果为负数，则需要返回32-result+num%2

class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        result = str(bin(num)).count('1')
        if(num>=0):
            return result
        else:
            return 32-result + num%2
#测试用例
if __name__ == '__main__':
    solution = Solution()
    #给定 32 (100000)，返回 1
    print(solution.countOnes(32))
    #给定 5 (101)，返回 2
    print(solution.countOnes(5))
    #给定 1023 (1111111111)，返回 10
    print(solution.countOnes(1023))
    #给定 0 (0)，返回 0
    print(solution.countOnes(0))
    #给定-1(11111111111111111111111111111111)，返回 32
    print(solution.countOnes(-1))
    #给定-178(11111111111111111111111101001110)，返回 28
    print(solution.countOnes(-178))