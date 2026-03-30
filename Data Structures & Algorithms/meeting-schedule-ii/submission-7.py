"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque 

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda i:i.start)
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        end.sort()
        s, e = 0, 0
        res = 0
        count = 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                count -=1
                e+=1
            res = max(res, count)
        
        return res
