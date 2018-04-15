/*
问题链接：
http://www.lintcode.com/zh-cn/problem/fizz-buzz/

问题描述：
给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

如果这个数被3整除，打印fizz.
如果这个数被5整除，打印buzz.
如果这个数能同时被3和5整除，打印fizz buzz.
*/



/*
 例子：
 比如 n = 15, 返回一个字符串数组：
 [
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]

 */

/**
 * @param n: An integer
 * @return: A list of strings.
 */
const fizzBuzz = function (n) {
  let results = [];
  for (let i = 0; i < n; i++) {
    let result = (i + 1).toString();
    if ((i + 1) % 3 === 0) {
      result = 'fizz';
    }
    if ((i + 1) % 5 === 0) {
      result = 'buzz';
    }
    if ((i + 1) % 3 === 0 && (i + 1) % 5 === 0) {
      result = 'fizz buzz';
    }
    results.push(result);
  };
  return results;
}


//测试用例：n=15

console.log('打印n=15的fizzBuzz:', fizzBuzz(15).join(','));

//运行：node index.js