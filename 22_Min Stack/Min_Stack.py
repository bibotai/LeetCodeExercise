"""
问题链接：
http://www.lintcode.com/en/problem/min-stack/

问题描述：
实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。
你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。
注意事项:如果堆栈中没有数字则不能进行min方法的调用

例如：
push(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 1，2，1
"""

#思路：
# 进栈时记录两个值，一个是进栈的数字，一个是当前进栈的数字与之前进栈数字相比 更小的值
# 出栈时按照先进后出，后进先出的方式出栈，出栈前输出当前出栈的数字
# min方法 只需返回进栈时计算的最后一个最小值
class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        if not self.stack:
            self.stack.append((number, number))
        else:
            self.stack.append((number, min(number, self.stack[-1][1])))

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if self.stack:
            result = self.stack[-1][0]
            self.stack.pop()
            return result
        else:
            return None

    """
    @return: An integer
    """

    def min(self):
        # write your code here
        if self.stack:
            return self.stack[-1][1]
        else:
            return None

#测试用例
if __name__ == '__main__':
    minstack = MinStack()
    # example :
    #push(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 1，2，1
    minstack.push(1)
    print(minstack.pop())
    minstack.push(2)
    minstack.push(3)
    print(minstack.min())
    minstack.push(1)
    print(minstack.min())
