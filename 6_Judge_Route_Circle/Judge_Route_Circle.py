"""
问题链接：
https://leetcode.com/problems/judge-route-circle/description/

问题描述：
开始的时候，在位置（0，0）上有一个机器人。给定一个动作序列，判断这个机器人是否做了一个圆圈，也即它能否移动回原来的位置。
动作序列用字符串表示。每一个动作都代表一个角色。有效的机器人动作是R（右），L（左），U（上）和D（下）。
输出应该是true或者false，表示机器人是否做圆周运动。


Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

"""
思路：
机器人 向左走的距离 = 向右走的距离 / 向上走的距离 = 向下走的距离 可能回到原地
时间复杂度 O(1)
空间复杂度 O(1)
"""
def judgeCircle_1(moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

def judgeCircle_2(moves):
    direct = {'U': 1, 'D': -1, 'L': 1j, 'R': -1j}
    return 0 == sum(direct[m] for m in moves)

#测试用例
if __name__ == '__main__':
    # Example 1:
    print(judgeCircle_1("UD"))
    print(judgeCircle_2("UD"))

    # Example 2:
    print(judgeCircle_1("LL"))
    print(judgeCircle_2("LL"))
