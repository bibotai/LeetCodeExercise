/*
问题链接：
https://leetcode.com/problems/merge-two-binary-trees/description/
问题描述：
给定两颗二叉树并假设当你将其中一颗尔盖另一颗树时，两棵树某些节点重叠而其他节点不重叠。

你需要将它们合并到新的二叉树中，合并规则是：如果两个节点重叠，则将节点值相加作为合并节点的新值。如果不重叠，非空节点将被用作新树的节点。
*/

/*
 例子：
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
*/

using System;
using System.Collections.Generic;

namespace Merge_Two_Binary_Trees
{
    class Program
    {
        /*
        方法＃1使用递归
        我们可以以预定的方式遍历给定的树。 在每一步中，我们检查当前节点是否存在（不为空）。
        如果为空，我们在两棵树的当前节点中添加值，并更新当前节点中的值以反映所获得的总和。 
        在每个步骤中，我们为这个节点的左孩子和右孩子调用原始函数mergeTree()。 
        如果在任何一个步骤中，其中一个孩子碰巧为空，我们会将另一棵树的子代表（代表相应的子树）作为子树添加到第一棵树中的调用父节点。 
        最后，第一棵树将代表所需的合成二叉树。

        */
        public static TreeNode mergeTrees1(TreeNode t1,TreeNode t2){
            if (t1==null)
                return t2;
            if (t2 == null)
                return t1;
            t1.val+=t2.val;
            t1.left= mergeTrees1(t1.left, t2.left);
            t1.right = mergeTrees1(t1.right, t2.right);
            return t1;
        }

        /*
        方法＃2使用迭代
        在这个方法中，我们使用一个堆栈。
        我们首先将两棵树的根节点推入堆栈。 然后，在每一步中，我们从栈顶移除一个节点对。 
        每删除一次节点对，我们相加对应这两个节点的值并更新第一个树中相应节点的值。 
        然后，如果第一棵树的左边有孩子存在，我们将两棵树的左边孩子（一对）压入堆叠。 
        如果第一个树的左侧子节点不存在，我们将第二个树的左侧子节点（子树）附加到第一个树的当前节点。 
        我们也对右子树做同样的事情。
        在任何步骤中，当前节点都是空的，我们继续从堆栈中弹出下一个节点。

        */
       
       public static TreeNode mergeTrees2(TreeNode t1,TreeNode t2){
            if (t1 == null)
            return t2;
            Stack <TreeNode[]> stack = new Stack<TreeNode[]> ();
            stack.Push(new TreeNode[] {t1, t2});
            while (stack.Count!=0) {
                TreeNode[] t = stack.Pop();
                if (t[0] == null || t[1] == null) {
                    continue;
                }
                t[0].val += t[1].val;
                if (t[0].left == null) {
                    t[0].left = t[1].left;
                } else {
                    stack.Push(new TreeNode[] {t[0].left, t[1].left});
                }
                if (t[0].right == null) {
                    t[0].right = t[1].right;
                } else {
                    stack.Push(new TreeNode[] {t[0].right, t[1].right});
                }
            }
            return t1;
        }
       

        static void Main(string[] args)
        {
            /*
            例子：
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
            */
            TreeNode t1=new TreeNode(1){
                left=new TreeNode(3){
                    left=new TreeNode(5), 
                },
                right=new TreeNode(2)
            };

            BTree btr1 = new BTree();
            btr1._root=t1;
            btr1._count=5;
            btr1.Print();

            TreeNode t2=new TreeNode(2){
                left=new TreeNode(1){
                    right=new TreeNode(4),
                },
                right=new TreeNode(3){
                    right=new TreeNode(7)
                }
            };
            BTree btr2 = new BTree();
            btr2._root=t2;
            btr2._count=5;
            btr2.Print();
            // Console.WriteLine("方法1：");
            // TreeNode result1=mergeTrees1(t1,t2);

            

            // BTree btr3 = new BTree();
            // btr3._root=result1;
            // btr3._count=9;
            // btr3.Print();



            Console.WriteLine("方法2：");
            TreeNode result2=mergeTrees2(t1,t2);

            BTree btr4 = new BTree();
            btr4._root=result2;
            btr4._count=9;
            btr4.Print();
        }
    }

    public class TreeNode{
        public int val { get; set; }
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int x) { val = x; }
        

    }



     public class BTree
    {
        public TreeNode _root;
        public int _count;
        private IComparer<int> _comparer = Comparer<int>.Default;


        public BTree()
        {
            _root = null;
            _count = 0;
        }

        public TreeNode Root { get { return _root; } }

        public void Print()
        {
            Root.Print();
        }
    
    }
    public static class BTreePrinter
    {
        class NodeInfo
        {
            public TreeNode Node;
            public string Text;
            public int StartPos;
            public int Size { get { return Text.Length; } }
            public int EndPos { get { return StartPos + Size; } set { StartPos = value - Size; } }
            public NodeInfo Parent, Left, Right;
        }

        public static void Print(this TreeNode root, string textFormat = "0", int spacing = 1, int topMargin = 2, int leftMargin = 2)
        {
            if (root == null) return;
            int rootTop = Console.CursorTop + topMargin;
            var last = new List<NodeInfo>();
            var next = root;
            for (int level = 0; next != null; level++)
            {
                var item = new NodeInfo { Node = next, Text = next.val.ToString(textFormat) };
                if (level < last.Count)
                {
                    item.StartPos = last[level].EndPos + spacing;
                    last[level] = item;
                }
                else
                {
                    item.StartPos = leftMargin;
                    last.Add(item);
                }
                if (level > 0)
                {
                    item.Parent = last[level - 1];
                    if (next == item.Parent.Node.left)
                    {
                        item.Parent.Left = item;
                        item.EndPos = Math.Max(item.EndPos, item.Parent.StartPos - 1);
                    }
                    else
                    {
                        item.Parent.Right = item;
                        item.StartPos = Math.Max(item.StartPos, item.Parent.EndPos + 1);
                    }
                }
                next = next.left ?? next.right;
                for (; next == null; item = item.Parent)
                {
                    int top = rootTop + 2 * level;
                    Print(item.Text, top, item.StartPos);
                    if (item.Left != null)
                    {
                        Print("/", top + 1, item.Left.EndPos);
                        Print("_", top, item.Left.EndPos + 1, item.StartPos);
                    }
                    if (item.Right != null)
                    {
                        Print("_", top, item.EndPos, item.Right.StartPos - 1);
                        Print("\\", top + 1, item.Right.StartPos - 1);
                    }
                    if (--level < 0) break;
                    if (item == item.Parent.Left)
                    {
                        item.Parent.StartPos = item.EndPos + 1;
                        next = item.Parent.Node.right;
                    }
                    else
                    {
                        if (item.Parent.Left == null)
                            item.Parent.EndPos = item.StartPos - 1;
                        else
                            item.Parent.StartPos += (item.StartPos - 1 - item.Parent.EndPos) / 2;
                    }
                }
            }
            Console.SetCursorPosition(0, rootTop + 2 * last.Count - 1);
        }

        private static void Print(string s, int top, int left, int right = -1)
        {
            Console.SetCursorPosition(left, top);
            if (right < 0) right = left + s.Length;
            while (Console.CursorLeft < right) Console.Write(s);
        }
    }

    
}
