"""
问题链接：
https://leetcode.com/problems/merge-two-binary-trees/description/

问题描述：
给定两个二叉树，想象当你把其中一个树覆盖另一个树时，这两棵树的一些节点是重叠的，而其他的不是。
你需要把它们合并成一个新的二叉树。合并规则是，如果两个节点重叠，则将节点值作为合并节点的新值。否则，非空节点将被用作新树的节点。

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

注意：合并过程必须从两个树的根节点开始。
"""

#需先安装binarytree：pip install binarytree
from binarytree import Node as TreeNode
from binarytree import build

class Solution:
    """
    思路1：把t1和t2合并成一个新树，并返回
    定义一个新树，给每个结点赋值为t1和t2对应节点的和，
    新树的根节点为两个树根节点之和。
    左子树递归，并把结果赋值给result->left。
    右子树递归，并把结果赋值给result->right。
    返回新树，即将两个树合并了。

    时间复杂度 O(n)
    空间复杂度 O(n)
    """
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Write your code here
        if not t1 and not t2:
            return None
        elif t1 and t2:
            result = TreeNode(t1.value + t2.value)
            result.left = self.mergeTrees(t1.left, t2.left)
            result.right = self.mergeTrees(t1.right, t2.right)
            return result
        else:
            return t1 or t2
#测试用例
if __name__ == '__main__':
    # example 1:
    tree1 = [1,3,2,5]
    tree2 = [2,1,3,None,4,None,7]
    my_tree1 = build(tree1)
    my_tree2 = build(tree2)
    TreeNode.pprint(my_tree1)
    TreeNode.pprint(my_tree2)
    TreeNode.pprint(Solution().mergeTrees(my_tree1,my_tree2))

    # tree2 为空:
    tree1 = [1,3,2,5]
    tree2 = []
    my_tree1 = build(tree1)
    my_tree2 = build(tree2)
    TreeNode.pprint(my_tree1)
    TreeNode.pprint(my_tree2)
    TreeNode.pprint(Solution().mergeTrees(my_tree1,my_tree2))


    # tree1和tree2 深度不同:
    tree1 = [1,3,2,5]
    tree2 = [1,2,4,3,2,1,6,9,12]
    my_tree1 = build(tree1)
    my_tree2 = build(tree2)
    TreeNode.pprint(my_tree1)
    TreeNode.pprint(my_tree2)
    TreeNode.pprint(Solution().mergeTrees(my_tree1,my_tree2))