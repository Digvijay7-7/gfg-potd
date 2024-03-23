'''
You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. Since the terms can become very large return the terms modulo 10^9+7.

Example 1:
Input:
n = 5
Output:
0 1 1 2 3 5
Explanation:
0 1 1 2 3 5 is the Fibonacci series up to the 5th term.

Example 2:
Input:
n = 10
Output:
0 1 1 2 3 5 8 13 21 34 55
Explanation:
0 1 1 2 3 5 8 13 21 34 55 is the Fibonacci series up to the 10th term.
Your Task:
You don't need to read input or print anything. Your task is to complete the function Series() which takes an Integer n as input and returns a Fibonacci series up to the nth term.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
'''

#User function Template for python3

class Solution:
    def series(self, n):
        MOD = 10**9 + 7  # Modulo value
        fibonacci_series = []  # List to store Fibonacci numbers
        a, b = 0, 1  # Initial Fibonacci numbers
        count = 0  # Counter to track the number of terms generated

        # Generate Fibonacci numbers up to the nth term
        while count <= n:
            fibonacci_series.append(a)
            a, b = b, (a + b) % MOD  # Update Fibonacci numbers with modulo
            count += 1

        return fibonacci_series


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends