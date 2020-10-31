"""
https://leetcode.com/problems/valid-anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
def isAnagram(s, t):
    return s.split(). sort() == t.split().sort()

print(isAnagram("anagram", "nagaram"))
print(isAnagram("car", "rat"))