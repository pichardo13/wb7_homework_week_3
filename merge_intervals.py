"""
https://leetcode.com/problems/merge-intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
def merge(intervals):
    intervals.sort() #sort based on the first item
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        inter = merged[-1] #the last item in iterval
        current = intervals[i]

        if inter[0] <= current[0] and current[0] <= inter[1]:
            merged[-1] = [inter[0], max(current[1], inter[1])]
        else:
            merged.append(current)

    return merged

print(merge([[15,18],[8,10],[2,6],[1,3]]))
print(merge([[1,4],[2, 3]]))
