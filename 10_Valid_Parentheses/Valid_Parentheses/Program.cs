using System;
using System.Collections.Generic;
/* 
问题链接：
https://leetcode.com/problems/merge-two-binary-trees/description/
问题描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串中括号是否正常的顺序关闭。

*/

namespace Valid_Parentheses
{
    class Program
    {
        /*
        解法：遇到一个前括号即入栈一个与之对应的后括号。遇到后括号出栈，判断出栈值是否等于后括号值。如不等即可返回false。
         */
        public static bool isValid(String s) {
        Stack<Char> stack = new Stack<Char>();
        foreach (char item in s.ToCharArray())
        {
            if (item == '(')
                stack.Push(')');
            else if (item == '{')
                stack.Push('}');
            else if (item == '[')
                stack.Push(']');
            else if (stack.Count==0 || stack.Pop() != item)
                return false;
        }
        if (stack.Count==0)
            return true;
        else
            return false;
}
        static void Main(string[] args)
        {
            Console.WriteLine("请输入字符串：");
            string s=Console.ReadLine();
            if (isValid(s))
            {
                Console.WriteLine("验证通过");
            }
            else
            {
                Console.WriteLine("验证不通过");
            }
        }
    }
}
