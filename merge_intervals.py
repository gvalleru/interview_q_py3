# Interval class which converts
class Interval:
    def __init__(self, interval_=[0, 0]):
        self.start = interval_[0]
        self.end = interval_[1]

    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)


class Solution:
    def merge(self, intervals):
        intervals = [Interval(i) for i in intervals]
        intervals.sort(key=lambda x: x.start)
        print intervals
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if interval.start <= stack[-1].end:
                    stack[-1].end = max(stack[-1].end, interval.end)
                else:
                    stack.append(interval)
        return stack
