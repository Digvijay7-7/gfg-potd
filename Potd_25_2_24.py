'''
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct combinations to reach the given score.

Example 1:
Input
n = 10
Output
2
Explanation
There are two ways {5,5} and {10}.

Example 2:
Input
n = 20
Output
4
Explanation
There are four possible ways. {5,5,5,5}, {3,3,3,3,3,5}, {10,10}, {5,5,10}.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function count( ) which takes n as input parameter and returns the answer to the problem.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 10^6
'''

#User function Template for python3

class Solution:
    def count(self, n: int) -> int:
        # Initialize dp array with zeros
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # There is one way to reach score 0
        
        # Iterate through scores from 3 to n
        for i in range(3, n + 1):
            dp[i] += dp[i - 3]  # Add combinations from moving 3 steps
        for i in range(5, n + 1):
            dp[i] += dp[i - 5]  # Add combinations from moving 5 steps
        for i in range(10, n + 1):
            dp[i] += dp[i - 10]  # Add combinations from moving 10 steps
        
        return dp[n]
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
# } Driver Code Ends