"""
https://leetcode.com/problems/house-robber-ii

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent 
houses were broken into on the same night.
Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [0]
Output: 0
"""

def rob(nums): 
    if len(nums) < 2:
        return nums
    elif len(nums) == 2:
        return max(nums)
    else:
        return max(helper(nums[1:]), nums[0] + helper(nums[2:-1]))

def helper(nums):
    arr = [0] * len(nums)

    for i in range(2, len(nums)):
        arr[i] = max(arr[i -1], arr[i] + arr[i-2])
    return arr[-1]

