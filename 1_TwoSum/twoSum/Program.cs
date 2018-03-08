//问题链接：
//https://leetcode.com/problems/two-sum/description/

//问题描述
//给定一个整数数组，返回两个数字的索引，使它们的和为一个特定的目标值。
//你可以认为每个输入都只有一个解决方案，并且你可能不会使用相同的元素两次。

//例子：

//Given nums = [2, 7, 11, 15], target = 9,
//Because nums[0] + nums[1] = 2 + 7 = 9,
//return [0, 1].

using System;
using System.Collections;

namespace twoSum
{
    class Program
    {
        //方法1 爆破
        //思路
        //暴力方法很简单。 遍历每个元素x并查找是否有另一个等于target的值 - x(target-x)。

        static int[] twoSum1(int[] nums, int target) {
            for (int i = 0; i < nums.Length; i++) {
                for (int j = i + 1; j < nums.Length; j++) {
                    if (nums[j] == target - nums[i]) {
                        return new int[] { i, j };
                    }
                }
            }
            throw new Exception("No two sum solution");
        }

        //时间复杂度：O(n^2)
        //空间复杂度：O(1)

        //方法2 双向哈希表
        //思路
        //为了提高运行时的复杂度，我们需要一种更有效的方法来检查数组中是否存在补码。如果存在，我们需要查找它的索引。
        //用于维护数组中每个元素到其索引的映射关系的数据结构是什么？哈希表！
        //我们通过牺牲空间来换取速度，我们把查找时间从 O(n) 降低到了 O(1)，哈希表正是为此目的而构建的，它支持在接近恒定的时间快速查找。
        //我说的接近，是因为如果发生碰撞，查找时间可以退化到O（n），但是，我们需要仔细选择哈希函数，在哈希表中的查找时间应该分摊到O（1）

        //一个简单的实现是使用两个迭代，第一次迭代，我们将每个元素的值和索引添加到一个哈希表中，第二次迭代，我们检查每个元素的补码（target - nums [i]）是否存在于表中。
        //注意补码不能是num [i]本身！
        static int[] twoSum2(int[] nums, int target) {
            Hashtable ht=new Hashtable();
            for (int i = 0; i < nums.Length; i++) {
                ht.Add(nums[i],i);
            }
            for (int i = 0; i < nums.Length; i++) {
                int complement = target - nums[i];
                if (ht.ContainsKey(complement) && (int)ht[complement] != i) {
                    return new int[] { i, (int)ht[complement] };
                }
            }
            throw new Exception("No two sum solution");
        }

        //时间复杂度：O(n)
        //空间复杂度：O(n)

        //方法3 单向哈希表
        //思路
        //实际上我们可以一次完成，当我们迭代并向哈希表中插入元素时，我们同时也检查一下哈希表中是否有当前元素的补码，如果存在立即返回。
        static int[] twoSum3(int[] nums, int target) {
            Hashtable ht=new Hashtable();
            for (int i = 0; i < nums.Length; i++) {
                int complement = target - nums[i];
                if (ht.ContainsKey(complement) && (int)ht[complement] != i) {
                    return new int[] { (int)ht[complement],i };
                }
                ht.Add(nums[i],i);
            }
            throw new Exception("No two sum solution");
        }

        //时间复杂度：O(n)
        //空间复杂度：O(n)

        //测试用例
        static void Main(string[] args)
        {
            int[] nums = new int[] {2, 7, 11, 15};
            Console.WriteLine("nums:{0}",String.Join(",",nums));
            int target=9;
            Console.WriteLine("target:{0}",target);
            Console.WriteLine("第一种方法：");
            Console.WriteLine(String.Join(", ",twoSum1(nums,target)));
            Console.WriteLine("第二种方法：");
            Console.WriteLine(String.Join(", ",twoSum2(nums,target)));
            Console.WriteLine("第三种方法：");
            Console.WriteLine(String.Join(", ",twoSum3(nums,target)));
        }
    }
}
