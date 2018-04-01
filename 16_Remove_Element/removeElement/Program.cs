using System;

/*
问题链接：
https://leetcode.com/problems/merge-two-binary-trees/description/
问题描述：
给定一个数组和一个值，在这个数组中原地移除指定值和返回移除后新的数组长度。

不要为其他数组分配额外空间，你必须使用 O(1) 的额外内存原地修改这个输入数组。

元素的顺序可以改变。超过返回的新的数组长度以外的数据无论是什么都没关系。
*/


/*
 例子：

给定 nums = [3,2,2,3]，val = 3，

你的函数应该返回 长度 = 2，数组的前两个元素是 2。

 */

namespace removeElement
{
    class Program
    {

        /*
        方法：使用两个指针

        题目要求我们原地移除给定的所有元素，又要保证 O(1)的空间复杂度，我们可以使用两个指针i和j
        i跑的慢一些，j跑的快一些。

        当nums[j]等于给定值，跳过它并且增加j的值，当nums[j]不等于给定值，我们把nums[j]拷贝到nums[i]上，同时增加两个指针的值。
        重复这个过程直到j到达数组的末尾，i就是新数组的长度。
        
         */


         public static int removeElement(int[] nums, int val) {
            int i = 0;
            for (int j = 0; j < nums.Length; j++) {
                if (nums[j] != val) {
                    nums[i] = nums[j];
                    i++;
                }
            }
            return i;
        }
        static void Main(string[] args)
        {
            int[] nums=new int[] {3,2,2,3};
            Console.WriteLine("给定数组："+string.Join(',',nums));
            Console.WriteLine("给定值：3");
            Console.WriteLine("移除元素后数组长度："+removeElement(nums,3));

        }
    }
}
