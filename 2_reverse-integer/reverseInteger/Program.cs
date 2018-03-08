//问题链接：
//https://leetcode.com/problems/reverse-integer/description/

//问题描述
//给出一个32位的整数，反转其中的数字。

//例子：

//Input: 123
//Output:  321

//Input: -123
//Output: -321

//注意：假设我们处在一个只能在32位有符号整数范围的环境，函数在反转时溢出返回0

using System;

namespace reverseInteger
{
    class Program
    {

        //思路：
        //通过 %取余获取到末端的数，通过/除法降位
        //如果数字溢出，newResult反推回去不对等于之前的结果。由此判断反转是否溢出。
        static int reverse(int x){
            int result = 0;
            int conut=1;
            while (x != 0)
            {
                int tail = x % 10;
                int newResult = result * 10 + tail;
                if ((newResult - tail) / 10 != result)
                { return 0; }
                Console.WriteLine(String.Format("这是第{0}次循环,tail = x % 10={1},newResult = result * 10 + tail={2}",conut,tail,newResult));
                result = newResult;
                x = x / 10;
                Console.WriteLine("x = x / 10="+x);
                conut++;
            }
            return result;

        }


        static void Main(string[] args)
        {
            Console.WriteLine("请输入数字：");
            int x=int.Parse(Console.ReadLine());
            Console.WriteLine("反转数字为：{0}",reverse(x));
        }
    }
}
