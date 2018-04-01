"""
问题链接：
https://leetcode.com/problems/interleaving-string/description/

问题描述：
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

例如，
给定：
s1 = "aabcc",
s2 = "dbbca",

当 s3 = "aadbbcbcac", 返回 true.
当 s3 = "aadbbbaccc", 返回 false.

"""
class Solution:
    # 使用一个二维数组 //计算所有可能的组合方式
    # 将所有的组合方式用boolean表示，最后一个位置的boolean值即能判断s3是否是由s1和s2交错形成的。
    # 时间复杂度O(m*n+m+n)
    # 空间复杂度O(m*n)
    def isInterleave_1(self, s1, s2, s3):
        c, r, l = len(s1), len(s2), len(s3)
        if c + r != l:
            return False
        elif c == 0:
            return s2 == s3
        elif r == 0:
            return s1 == s3
        else:
            dp = [[True for row in range(c + 1)] for col in range(r + 1)]
            for i in range(1, r + 1):
                #第0列每一行的值 为 s1是否与s3匹配的boolean值
                dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            for j in range(1, c + 1):
                #第0行每一列的值 为 s2是否与s3匹配的boolean值
                dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            for i in range(1, r + 1):
                for j in range(1, c + 1):
                    # 第i行第j列的值 为 s1/s2是否与s3匹配的boolean值
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or \
                               (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
            return dp[-1][-1]

    # 使用两个一维数组 //计算所有可能的组合方式
    # 将是否交错的计算结果计入一个数组cur，再将这个数组的结果赋值给另一个数组pre。[计算时使用这两个数组]
    # 时间复杂度O(m*(n+1))
    # 空间复杂度O(n*2)
    def isInterleave_2(self, s1, s2, s3):
        l1, l2, l3 = len(s1) + 1, len(s2) + 1, len(s3) + 1
        if l1 + l2 != l3 + 1:
            return False
        elif l1 == 1:
            return s2 == s3
        elif l2 == 1:
            return s1 == s3
        else:
            pre = [True for _ in range(l2)]
            for j in range(1, l2):
                pre[j] = pre[j - 1] and s2[j - 1] == s3[j - 1]
            for i in range(1, l1):
                cur = [pre[0] and s1[i - 1] == s3[i - 1]] * l2
                for j in range(1, l2):
                    cur[j] = (cur[j - 1] and s2[j - 1] == s3[i + j - 1]) or \
                             (pre[j] and s1[i - 1] == s3[i + j - 1])
                #数组复制 pre和cur是两个完全独立的数组互相不会影响
                pre = cur[:]
        return pre[-1]

    # 使用一个一维数组 //计算所有可能的组合方式
    # 将是否交错的计算结果计入数组dp。[计算时也仅使用这一个数组]
    # 时间复杂度O(m*(n+1))
    # 空间复杂度O(n)
    def isInterleave_3(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        elif r == 0:
            return s2 == s3
        elif c == 0:
            return s1 == s3
        else:
            dp = [True for _ in range(c + 1)]
            for j in range(1, c + 1):
                dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            for i in range(1, r + 1):
                dp[0] = (dp[0] and s1[i - 1] == s3[i - 1])
                for j in range(1, c + 1):
                    dp[j] = (dp[j] and s1[i - 1] == s3[i - 1 + j]) or (dp[j - 1] and s2[j - 1] == s3[i - 1 + j])
            return dp[-1]

    # 深度优先搜索 DFS【* 针对此题来说 时间复杂度最小】
    # 其过程简要来说是对每一个可能的分支路径深入到不能再深入为止 而且每个节点只能访问一次
    def isInterleave_4(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        elif r == 0:
            return s2 == s3
        elif c == 0:
            return s1 == s3
        else:
            stack, visited = [(0, 0)], set((0, 0))
            while stack: # 栈：先进后出
                x, y = stack.pop() #出栈
                if x + y == l:
                    return True
                if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                    stack.append((x + 1, y)) #入栈,记录位置
                    visited.add((x + 1, y))
                if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                    stack.append((x, y + 1)) #入栈，记录位置
                    visited.add((x, y + 1))
            return False

    # 广度优先搜索 BFS
    # 广度优先搜索并不考虑结果的可能位置 彻底地搜索整张图 直到找到结果为止
    # 从算法的观点，所有因为展开节点而得到的子节点都会被加进一个先进先出的队列中。
    # 一般的实验里，其邻居节点尚未被检验过的节点会被放置在一个被称为 open 的容器中（例如队列或是链表），而被检验过的节点则被放置在被称为 closed 的容器中。
    def isInterleave_5(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        elif r == 0:
            return s2 == s3
        elif c == 0:
            return s1 == s3
        else:
            queue, visited = [(0, 0)], set((0, 0))
            while queue: #队列：先进先出
                x, y = queue.pop(0) #出队列
                if x + y == l:
                    return True
                if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                    queue.append((x + 1, y)) #加入队列
                    visited.add((x + 1, y))
                if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                    queue.append((x, y + 1)) #加入队列
                    visited.add((x, y + 1))
            return False
#测试用例
if __name__ == '__main__':
    interleaving = Solution()

    print("testcase_1:")
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(interleaving.isInterleave_1(s1,s2,s3))
    print(interleaving.isInterleave_2(s1,s2,s3))
    print(interleaving.isInterleave_3(s1,s2,s3))
    print(interleaving.isInterleave_4(s1,s2,s3))
    print(interleaving.isInterleave_5(s1,s2,s3))
    #预期 True

    print("testcase_2:")
    s3 = "aadbbbaccc"
    print(interleaving.isInterleave_1(s1,s2,s3))
    print(interleaving.isInterleave_2(s1,s2,s3))
    print(interleaving.isInterleave_3(s1,s2,s3))
    print(interleaving.isInterleave_4(s1,s2,s3))
    print(interleaving.isInterleave_5(s1,s2,s3))
    #预期 False

    print("testcase_3:")
    s1 = "aabcc"
    s2 = "a"
    s3 = "aadbbcbcac"
    print(interleaving.isInterleave_1(s1, s2, s3))
    print(interleaving.isInterleave_2(s1, s2, s3))
    print(interleaving.isInterleave_3(s1, s2, s3))
    print(interleaving.isInterleave_4(s1, s2, s3))
    print(interleaving.isInterleave_5(s1, s2, s3))
    #预期 False


    print("testcase_4:")
    s1 = "adbcc"
    s2 = ""
    s3 = "adbcc"
    print(interleaving.isInterleave_1(s1, s2, s3))
    print(interleaving.isInterleave_2(s1, s2, s3))
    print(interleaving.isInterleave_3(s1, s2, s3))
    print(interleaving.isInterleave_4(s1, s2, s3))
    print(interleaving.isInterleave_5(s1, s2, s3))
    #预期 True