"""
问题链接：
https://www.lintcode.com/zh-cn/problem/insert-interval/

问题描述：
插入区间
给定一个非重叠的间隔列表，该列表起始点排序。
在其中插入一个新的间隔，确保列表仍然是有序的和不重叠的（如果需要的话，合并间隔）。

样例
将 (2, 5) 插入 [(1,2), (5,9)], 返回 [(1,9)].
将 (3, 4) 插入 [(1,2), (5,9)], 返回 [(1,2), (3,4), (5,9)].
"""

#思路：
#如果新间隔的start比旧间隔列表中某一个间隔的end大，则将这个间隔加入新间隔列表中 新间隔插入位置+1
#如果新间隔的end比旧间隔列表中某一个间隔的start小，则将这个间隔加入新间隔列表中
#反之，让新间隔的start=新旧间隔的最小值；end=新旧间隔的最大值
#最后将新间隔插入对应的位置，即可得到新的间隔列表

#Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def show(self):
        return "("+str(self.start)+","+str(self.end)+")"

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        newintervals = []
        insertPos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                newintervals.append(interval)
                insertPos += 1
            elif interval.start > newInterval.end:
                newintervals.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        newintervals.insert(insertPos, newInterval)
        return newintervals
#测试用例
if __name__ == '__main__':
    solution = Solution()
    intervals = [Interval(1,2), Interval(5,9)]
    newInterval = Interval(2,5)
    results = solution.insert(intervals,newInterval)
    print(results)
    newintervals = []
    for result in results:
        newintervals.append(result.show())
    print(newintervals)

    intervals = [Interval(1, 2), Interval(5, 9)]
    newInterval = Interval(3, 4)
    results = solution.insert(intervals, newInterval)
    print(results)
    newintervals = []
    for result in results:
        newintervals.append(result.show())
    print(newintervals)

    intervals = [Interval(1, 5)]
    newInterval = Interval(5, 7)
    results = solution.insert(intervals, newInterval)
    print(results)
    newintervals = []
    for result in results:
        newintervals.append(result.show())
    print(newintervals)
