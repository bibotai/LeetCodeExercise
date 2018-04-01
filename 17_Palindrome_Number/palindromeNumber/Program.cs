﻿using System;

/*
问题链接：
https://leetcode.com/problems/palindrome-number/description/

问题描述：
判断一个整数是否是回文数。不能使用辅助空间。

一些提示:

负整数可以是回文数吗？（例如 -1）

如果你打算把整数转为字符串，请注意不允许使用辅助空间的限制。

你也可以考虑将数字颠倒。但是如果你已经解决了 “颠倒整数” 问题的话，就会注意到颠倒整数时可能会发生溢出。你怎么来解决这个问题呢？

本题有一种比较通用的解决方式。
*/



/*
 例子：

1221、123321

 */


namespace palindromeNumber
{
    class Program
    {
        /*
        思路：
        首先想到的想法是将数字转换为字符串，并检查字符串是否是回文，但这需要额外的非常量空间来创建字符串，这是问题描述所不允许的。

        第二个想法是反转数字本身，然后将反转后的数字与原始数字进行比较，如果它们相同，则数字是回文。但是，如果颠倒的数字大于
        int.MAX，我们会碰到整数溢出问题。

        根据第二个想法，为了避免已反转数字的溢出问题，我们只反转一半，毕竟，如果数字是回文，回文后半部分的反转应与数字的前半部分相同。

        例如，如果输入是1221，如果我们可以将数字“1221”的最后部分从“21”反转到“12”，并将其与数字“12”的前半部分进行比较，
        我们知道这个数字是一个回文。

        首先，我们应该关注一些边缘案例。所有负数不是回文，例如：-123不是回文，因为' - '不等于'3'。所以我们可以为所有负数返回false。

        现在让我们考虑如何反转数字的后半部分。对于数字1221，如果我们做1221％10，我们得到最后一位数字1，
        
        为了得到第二位数字，我们需要从1221中删除最后一位数字，我们可以通过除以10,1221 / 10 = 122.
        
        然后我们可以通过取余 122％10 = 2为模数再次得到最后一位数，
        
        如果我们将最后一位数乘以10并加上第二位数，即1 * 10 + 2 = 12，这就是我们想要反转的数字。继续这个过程会给我们更多数字的反转。

        现在的问题是，我们怎么知道我们已经达到了这个数字的一半呢？

        由于我们将数字除以10，并将反转数字乘以10，当原始数字小于反转数字时，这意味着我们已经处理了一半的数字。

         */


        public static bool IsPalindrome(int x) {
            
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        
        int revertedNumber = 0;
        while(x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        
        //当长度为奇数时，我们可以通过revertedNumber / 10来消除中间数字
        //例如，当输入是12321时，在while循环结束时，我们得到x = 12，revertedNumber = 123，
        //因为中间数字在palidrome中并不重要（它总是等于它本身），所以我们可以简单地将其除掉。
        return x == revertedNumber || x == revertedNumber/10;
    }
        static void Main(string[] args)
        {
            Console.WriteLine("判断数字是否是回文数字");

            Console.WriteLine("请输入一段数字：");
            int num=int.Parse(Console.ReadLine());
            if (IsPalindrome(num))
            {
                Console.WriteLine("是回文数字");
            }
            else
            {
                Console.WriteLine("不是回文数字");
            }
        }
    }
}
