"""
问题链接：
https://leetcode.com/problems/hamming-distance/description/

问题描述：
两个整数之间的汉明距离是对应位不同的位置数。
换句话说，它就是将一个整数变换成另外一个整数所需要替换的字符个数。

给定两个整数x和y，计算汉明距离。

注:
0 ≤ x, y < 2^31.

例:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上述箭头指向相应比特不同的位置。
"""

"""
思路1：
将x与y进行异或运算，结果计入b
计算c中包含多少个1，也即x与y的汉明距离
时间复杂度 O(n)
空间复杂度 O(1)
"""
def hamming_distance_test1(x,y):
    if (x>=0 and y>=0 and x<2147483648 and y<2147483648):
        """
        c = 0
        b = bin(x ^ y)[2:]
        for i in range(0,len(b)):
        if(b[i]=='1'):
            c+=1
        return c
        """
        #写成一行
        return bin(x ^ y).count('1')
    else:
        return "0 ≤ x, y < 2^31"

"""
思路2：
将x与y转换为位数相同的二进制数
使用python内置函数zip
  zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
  如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。
一个个遍历来判断元组中的值是否相同，返回不同的个数

或者直接使用for i in range(0,len(binx)) 判断binx[i]和biny[i]是否相同

时间复杂度 O(2n)
空间复杂度 O(1)
"""
def hamming_distance_test2(x,y):
    if (x >= 0 and y >= 0 and x < 2147483648 and y < 2147483648):
        binx = bin(x)[2:]
        biny = bin(y)[2:]
        if (len(binx) > len(biny)):
            for i in range(0, len(binx) - len(biny)):
                biny = "0" + biny
        elif (len(biny) > len(binx)):
            for i in range(0, len(biny) - len(binx)):
                binx = "0" + binx
        """
        count=0
        for i in range(0,len(binx)):
            if(binx[i]!=biny[i]):
                count+=1
        return count
        """
        #写成一行
        return sum(el1 != el2 for el1, el2 in zip(binx, biny))
    else:
        return "0 ≤ x, y < 2^31"


#测试用例
if __name__ == '__main__':
    print("2^31="+str(2**31))

    #Example 1:
    x=1
    y=4
    print(hamming_distance_test1(x, y))
    print(hamming_distance_test2(x, y))

    #其他数值:
    x=255
    y=164
    print(hamming_distance_test1(x, y))
    print(hamming_distance_test2(x, y))

    # x/y<0:
    x = -1
    y = 19
    print(hamming_distance_test1(x, y))
    print(hamming_distance_test2(x, y))

    #x/y>=2^31  2147483648:
    x=2147483648
    y=2147483649
    print(hamming_distance_test1(x, y))
    print(hamming_distance_test2(x, y))