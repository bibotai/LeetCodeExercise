"""
问题链接：
https://leetcode.com/problems/merge-two-sorted-lists/description/

问题描述：
合并两个已排序的链表并将其作为一个新链表返回。新链表应该通过拼接前两个链表的节点来完成。

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# coding:utf-8
# Definition for singly-linked list.定义单向链表
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ListOP:
    #创建链表
    def createlist(self,list):
        l = ListNode(list[0])
        p = l
        for i in list[1:]:
            p.next = ListNode(i)
            p = p.next
        return l

    #输出链表
    def printlist(self,r):
        result = ""
        while (r != None):
            result += str(r.val)
            if (r.next != None):
                result += "->"
            r = r.next
        print(result)

class Solution(object):
    """
    思路1：迭代，重复操作某些步骤，达到想要的目的。
    定义一个新的链表
    对比两个链表的值，如果l1比l2小，则新链表的next=l1当前的值，l1 = l1.next；反之新链表的next=l2当前值，l2=l2.next
    如此迭代循环，直到l1和l2中有一个为空。
    新链表的next = l1和l2中不为空的链表。
    返回新链表，即将两个已排序的链表合并了。
    时间复杂度 O(n)
    空间复杂度 O(1)
    """
    def mergeTwoLists_1(self, l1, l2):
        dummy = cur = ListNode(0)
        #两个链表都不为空时执行以下循环
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        #cur.next=l1和l2中不为空的链表
        cur.next = l1 or l2
        return dummy.next

    """
    思路2：递归，自身调用自身的迭代就。
    对比两个链表的值，如果l1比l2小，则l1 = l1.next，返回l1；反之l2=l2.next，返回l2。
    递归循环这个函数，直到l1和l2中有一个为空，返回不为空的值。
    最终返回的值即为合并后的链表
    
    时间复杂度 O(n)
    空间复杂度 O(1)
    """
    def mergeTwoLists_2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists_2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_2(l1, l2.next)
            return l2

#测试用例
if __name__ == '__main__':
    #print("输入两个链表，用->分割链表值，用,分割两个链表：")
    lists = input()
    # 输入
    # example 1:
    #1->2->4, 1->3->4

    # 除头外，没有不重复的数字:
    #1->2->4, 1->3->5

    # 所有数字都不同：
    #2->4->7, 1->3->5

    #将输入的数据分割，放入数组中
    arr = lists.split(", ")
    arr1 = arr[0].split("->")
    arr2 = arr[1].split("->")
    #将数组中的数据放入链表中
    l1 = ListOP().createlist(arr1)
    l2 = ListOP().createlist(arr2)

    # 合并两个链表
    # 单向链表 故 以下两种方法一次只能执行一个
    #q = s.mergeTwoLists_1(l1, l2)
    r = Solution().mergeTwoLists_2(l1, l2)
    #输出合并后的链表
    ListOP().printlist(r)

    # 输出：
    # example 1:
    #1->1->2->3->4->4

    # 除头外，没有不重复的数字:
    #1->1->2->3->4->5

    # 所有数字都不同：
    #1->2->3->3->5->7