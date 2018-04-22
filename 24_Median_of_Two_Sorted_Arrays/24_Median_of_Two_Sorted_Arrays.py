# coding:utf-8
"""
问题链接：
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

问题描述：
找出两个升序排序的数组的中间值

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
思路：
二分法速度最快，找到最左边的值+1，最右边的值-1
"""

def median(A, B):
    m,n = len(A),len(B)#m,n为A，B的长度
    if m > n:
        A,B,m,n =B,A,n,m#为了保证B数组长于A数组，进行一下互换
    if n == 0:
        return 0#如果小的数组=0，那就没法继续了
    imin,imax,half_len = 0,m,(m+n+1)/2 #接下来准备用二分法找到i值。
                                # 如果把两个数组合并，如果m+n为偶数，
                                # 需要找到的这个值应该为(half_len+half_len[+1])/2
                                # 如果为奇数，half_len就是要找的数
    while imin <= imax:
        i = (imin+imax)/2#二分法
        j = half_len - i#i是A的分界点，j是B的分界点，i的左边+j的左边=i的右边+j的右边=half_len
                        #i增大，j减小
        if i < m and A[i] < B[j-1]:
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            imax = i - 1
        else:
            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i -1],B[j -1])

            if(m + n )%2 ==1:#如果m+n为奇数
                return max_of_left
            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i],B[j])
            return (max_of_left+min_of_right)/2.0
if __name__ == '__main__':
    a = [1,2,3,6,7,8,9]
    b = [2,3,4,7,8,9]
    print median(a,b)