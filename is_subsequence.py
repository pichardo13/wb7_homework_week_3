"""
https://leetcode.com/problems/is-subsequence/description/


Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence 
of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has 
its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""
#Step 1: make a matrix on len m + 1 by n + 1 filled with 0
#Step 2: compare 
def longestSub(s,t):
    m = len(s) + 1
    n = len(t) + 1
    matrix = [[0] * n for i in range(m)]

    for i in range(m):
        for j in range(n):
            if i != 0 and j != 0:
                if s[i - 1] == t[j - 1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[m - 1][n - 1] == len(s)

def isSubsequence(s, t):
    return longestSub(s,t)

print(isSubsequence('abc', "ahbgdc"))
print(isSubsequence('axc', 'ahbgdc'))
