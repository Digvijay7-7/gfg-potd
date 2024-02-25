'''
Given two strings s and t of length n and m respectively. Find the count of distinct occurrences of t in s as a sub-sequence modulo 109 + 7.

Example 1:
Input:
s = "banana" , t = "ban"
Output: 
3
Explanation: 
There are 3 sub-sequences:[ban], [ba n], [b an].

Example 2:
Input:
s = "geeksforgeeks" , t = "ge"
Output: 
6
Explanation: 
There are 6 sub-sequences:[ge], [ge], [g e], [g e] [g e] and [g e].
Your Task:
You don't need to read input or print anything.Your task is to complete the function subsequenceCount() which takes two strings as argument s and t and returns the count of the sub-sequences modulo 109 + 7.

Expected Time Complexity: O(n*m).
Expected Auxiliary Space: O(n*m).

Constraints:
1 ≤ n,m ≤ 1000
'''

# Your task is to complete this function
# Finction should return Integer
class Solution:
    def sequenceCount(self,s, t):
        MOD = 10**9 + 7
        n, m = len(s), len(t)
        
        # Create a 1D array to store counts for the current prefix of s
        dp = [0] * (m + 1)
        dp[0] = 1
        
        # Iterate through each character of s
        for char in s:
            # Iterate backwards through each character of t
            for j in range(m, 0, -1):
                # If the characters match, update the count
                if char == t[j - 1]:
                    dp[j] = (dp[j] + dp[j - 1]) % MOD
        
        return dp[m]

#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends