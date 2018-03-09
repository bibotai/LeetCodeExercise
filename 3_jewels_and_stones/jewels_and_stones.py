"""
问题链接：
https://leetcode.com/problems/jewels-and-stones/description/

问题描述：
珠宝&石头
珠宝是石头的一种类型，字符串J代表珠宝，字符串S代表石头，每一个S内的字符都代表石头的一种类型。
需要计算的是【石头中包含多少珠宝】

注：
1.J中的字符是不同的，J和S中所有的字符都是字母。
2.字母是区分大小写的，也即a和A是不同类型的石头。
3.J和S均包含字母，最多有50的长度。

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

"""
import re
"""
思路1：爆破
遍历每个元素，判断在J中出现了多少次S
时间复杂度：O(n^2)
空间复杂度：O(1)
"""
def numJewelsInStones_test1(J, S):
    #满足条件才执行计算
    if(type(J)==str and type(S)==str and re.match(r"[a-zA-Z]{"+str(len(J))+"}",J) and re.match(r"[a-zA-Z]{"+str(len(S))+"}",S) and len(J)<50 and len(S)<50):
        """
        #代码分解：
        count = 0
        for s in S:
            for j in J:
                if(s==j):
                    print(s+" "+j)
                    count+=1
        return count
        """
        #写成1行：
        return sum(s in J for s in S)
    else:
        return "S and J will consist of letters and have length at most 50"


"""
思路2：使用python内置函数map用映射来解决
map() 是python的内置函数，它会根据提供的函数对指定序列做映射。
语法：map(function, iterable, ...)
参数：
  function -- 函数，有两个参数
  iterable -- 一个或多个序列
  
iterable中的每一个元素都会调用function函数，返回值为每次function函数返回值的新列表

Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
语法：str.count(sub, start= 0,end=len(str))

时间复杂度 O(n)
空间复杂度 O(n)
"""
def numJewelsInStones_test2(J, S):
    # 满足条件才执行计算
    if(type(J)==str and type(S)==str and re.match(r"[a-zA-Z]{"+str(len(J))+"}",J) and re.match(r"[a-zA-Z]{"+str(len(S))+"}",S) and len(J)<50 and len(S)<50):
        """
        #代码分解：
        sum = 0
        for j in J:
            sum+=S.count(j, 0, len(S))
        return sum
        """
        #写成一行：（下边两行一个意思）
        #return sum(map(S.count, J))
        return sum(map(J.count, S))
    else:
        return "S and J will consist of letters and have length at most 50"

#测试用例
if __name__ == '__main__':
    #Example 1:
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones_test1(J, S))
    print(numJewelsInStones_test2(J, S))

    #Example 2:
    J = "z"
    S = "ZZ"
    print(numJewelsInStones_test1(J, S))
    print(numJewelsInStones_test2(J, S))

    #字符串过长
    J = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY"
    S = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZZzzz"
    print(numJewelsInStones_test1(J, S))
    print(numJewelsInStones_test2(J, S))

    #字符串中包含除了字母之外的东西
    J = "abcFGHIJKLMNOPQRY2"
    S = "abcFGHIJKLMNOPQRSTUVWXY1,"
    print(numJewelsInStones_test1(J, S))
    print(numJewelsInStones_test2(J, S))
