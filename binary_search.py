"""
https://leetcode.com/problems/binary-search/description/

Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1: 
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
def binarySearch(nums, target, left, right):
    mid = (right + left) // 2
    if left > right:
        return -1
    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return binarySearch(nums, target, mid + 1, right)
    elif nums[mid] > target:
        return binarySearch(nums, target, left, mid - 1)
    

def search(nums, target):
    return binarySearch(nums, target, 0, len(nums) - 1)

print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))
    

