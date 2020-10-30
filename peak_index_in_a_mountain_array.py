"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Let's call an array arr a mountain if the following properties hold:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... arr[i-1] < arr[i]
        arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array arr that is guaranteed to be a mountain, return any i such that 
arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1

Example 4:
Input: arr = [3,4,5,1]
Output: 2

Example 5:
Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2
"""
def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (right - left) // 2 + 1
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        if arr[mid] > arr[left]:
            left = mid - 1
        if arr[mid] > arr[right]:
            right = mid + 1

    return right

    # while left < right:
    #     if arr[left] < arr[mid]:
    #         left += 1
    #     if arr[right] < arr[mid]:
    #         right -= 1
    #     mid = left + (right - left) // 2
    
    # return mid

    #has several bugs
print(peakIndexInMountainArray([0,10,5,2]))
print(peakIndexInMountainArray([3,4,5,1]))
print(peakIndexInMountainArray([24, 69, 100, 99,79, 67, 36,0]))