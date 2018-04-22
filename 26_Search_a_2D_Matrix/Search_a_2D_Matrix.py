"""
问题链接：
http://www.lintcode.com/en/problem/search-a-2d-matrix/

问题描述：
搜索二维矩阵
写出一个高效的算法来搜索 m × n矩阵中的值。
这个矩阵具有以下特性：
每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。

例如：
[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
给出 target = 3，返回 true

"""

#思路：
# 一共分五种情况
# 1.martix 为空 返回false
# 2.martix 只有1行 只需返回第一行中是否包含target
# 3.martix 有多行 且target比第一行的第一个数字小 返回false
# 4.martix 有多行 且target比最后一行的第一个数字大 返回最后一行是否包含target
# 5.martix 有多行 且target的大小在某两行的第一个数字之间 返回较小的那一行是否包含target
# min方法 只需返回进栈时计算的最后一个最小值
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix)==0:
            return False
        elif len(matrix)==1:
            return target in matrix[0]
        elif target<matrix[0][0]:
            return False
        elif target>=matrix[len(matrix)-1][0]:
            return target in matrix[len(matrix)-1]
        for i in range(1,len(matrix)):
            if target< matrix[i][0] and target>= matrix[i-1][0]:
                return target in matrix[i-1]
#测试用例
if __name__ == '__main__':
    solution = Solution()
    """
    例如：
        [
          [1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        给出 target = 3，返回 true
    """
    matrix = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]]
    target = 3
    print(solution.searchMatrix(matrix,target))

    """
    例如：
        [
          [1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        给出 target = 0，返回 false
    """
    matrix = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]]
    target = 0
    print(solution.searchMatrix(matrix,target))

    """
        例如：
            []
            给出 target = 2，返回 false
    """
    matrix = []
    target = 2
    print(solution.searchMatrix(matrix, target))

    """
        例如：
            [[5]]
            给出 target = 2，返回 false
    """
    matrix = [[5]]
    target = 2
    print(solution.searchMatrix(matrix, target))

    """
        例如：
            [[5]]
            给出 target = 5，返回 true
    """
    matrix = [[5]]
    target = 5
    print(solution.searchMatrix(matrix, target))

    """
        例如：
            [
                [1,2,8,10,16,21,23,30,31,37,39,43,44,46,53,59,66,68,71],
                [90,113,125,138,157,182,207,229,242,267,289,308,331,346,370,392,415,429,440],
                [460,478,494,506,527,549,561,586,609,629,649,665,683,704,729,747,763,786,796],
                [808,830,844,864,889,906,928,947,962,976,998,1016,1037,1058,1080,1093,1111,1136,1157],
                [1180,1204,1220,1235,1251,1272,1286,1298,1320,1338,1362,1378,1402,1416,1441,1456,1475,1488,1513],
                [1533,1548,1563,1586,1609,1634,1656,1667,1681,1706,1731,1746,1760,1778,1794,1815,1830,1846,1861]
            ]
            给出 target = 1861，返回 true
    """
    matrix = [[1,2,8,10,16,21,23,30,31,37,39,43,44,46,53,59,66,68,71],[90,113,125,138,157,182,207,229,242,267,289,308,331,346,370,392,415,429,440],[460,478,494,506,527,549,561,586,609,629,649,665,683,704,729,747,763,786,796],[808,830,844,864,889,906,928,947,962,976,998,1016,1037,1058,1080,1093,1111,1136,1157],[1180,1204,1220,1235,1251,1272,1286,1298,1320,1338,1362,1378,1402,1416,1441,1456,1475,1488,1513],[1533,1548,1563,1586,1609,1634,1656,1667,1681,1706,1731,1746,1760,1778,1794,1815,1830,1846,1861]]
    target = 1861
    print(solution.searchMatrix(matrix, target))

