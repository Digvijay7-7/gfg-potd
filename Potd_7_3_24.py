'''
Given a string s of length n, find the longest repeating non-overlapping substring in it. In other words find 2 identical substrings of maximum length which do not overlap. Return the longest non-overlapping substring. Return "-1" if no such string exists.

Note: Multiple Answers are possible but you have to return the substring whose first occurrence is earlier.

For Example: "abhihiab", here both "ab" and "hi" are possible answers. But you will have to return "ab" because it's first occurrence appears before the first occurrence of "hi".

Example 1:
Input:
n = 9
s = "acdcdacdc"
Output:
"acdc"
Explanation:
The string "acdc" is the longest Substring of s which is repeating but not overlapping.

Example 2:
Input:
n = 7
s = "heheheh"
Output:
"heh"
Explanation:
The string "heh" is the longest Substring of s which is repeating but not overlapping.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestSubstring() which takes an Integer n and a string s as input and returns the answer.

Expected Time Complexity: O(n^2)
Expected Auxiliary Space: O(n^2)
'''

#User function Template for python3
class Solution:
    def longestSubstring(self, s, n):
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        max_len = 0
        end_idx = 0
        
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if s[i - 1] == s[j - 1] and dp[i - 1][j - 1] < j - i:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_idx = i - 1
                else:
                    dp[i][j] = 0        
        if max_len == 0:
            return "-1"
        else:
            return s[end_idx - max_len + 1: end_idx + 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S , N))
# } Driver Code Ends