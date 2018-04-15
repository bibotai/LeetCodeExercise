/*
问题链接：
http://www.lintcode.com/zh-cn/problem/fibonacci/

问题描述：
查找斐波纳契数列中第 N 个数。

所谓的斐波纳契数列是指：

前2个数是 0 和 1 。
第 i 个数是第 i-1 个数和第i-2 个数的和。
斐波纳契数列的前10个数字是：

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
*/



/*
 例子：

给定 1，返回 0

给定 2，返回 1

给定 10，返回 34

 */

//方法1：递归

//根据斐波纳契数列前十个数可知，第一个是0 第二个是1  如果n=1或2直接返回，
//如果n>2可以用递归法相加fibonacci(n-1)+fibonacci(n-2)的值
//但是此方法提交到lintcode中运行时间超时，说明时间复杂度太高。

/**
 * @param n: an integer
 * @return: an ineger f(n)
 */
const fibonacci = function (n) {
  if (n === 1) {
    return 0;
  }
  if (n === 2) {
    return 1;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2)
  }
}


//方法2：for循环

//根据斐波纳契数列前十个数可知，第一个是0 第二个是1  如果n=1或2直接返回，
//使用两个变量分别保存f(n-1) 和f (n-2)，然后从基准情况开始往第 n 个数推进

/**
 * @param n: an integer
 * @return: an ineger f(n)
 */
const fibonacci1 = function (n) {
  if (n === 1) {
    return 0;
  }
  if (n === 2) {
    return 1;
  }
  let a = 0;
  let b = 1;
  let c = 0;
  for (let i = 3; i < n + 1; i++) {
    c = a + b;
    a = b;
    b = c;
  }

  return c;

}

//测试用例 n=45

console.log('使用方法1 n=45');

let startTime=new Date();

console.log(fibonacci(45));

let endTime=new Date();

console.log('方法1用时：'+parseInt(endTime - startTime) / 1000+'秒');

console.log('使用方法2 n=45');

let startTime1=new Date();

console.log(fibonacci1(45));


let endTime1=new Date();

console.log('方法1用时：'+parseInt(endTime1 - startTime1) / 1000+'秒');

// 运行：node index.js