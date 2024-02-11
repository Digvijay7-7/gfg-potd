'''
Given a nxn matrix such that each of its cells contains some coins. Count the number of ways to collect exactly k coins while moving from top left corner of the matrix to the bottom right. From a cell (i, j), you can only move to (i+1, j) or (i, j+1).

Example 1:
Input:
k = 12, n = 3
arr[] = [[1, 2, 3], 
       [4, 6, 5], 
       [3, 2, 1]]
Output: 
2
Explanation: 
There are 2 possible paths with exactly 12 coins, (1 + 2 + 6 + 2 + 1) and (1 + 2 + 3 + 5 + 1).

Example 2:
Input:
k = 16, n = 3
arr[] = [[1, 2, 3], 
       [4, 6, 5], 
       [9, 8, 7]]
Output: 
0 
Explanation: 
There are no possible paths that lead to sum=16

Your Task:  
You don't need to read input or print anything. Your task is to complete the function numberOfPath() which takes n, k and 2D matrix arr[][] as input parameters and returns the number of possible paths.

Expected Time Complexity: O(n*n*k)
Expected Auxiliary Space: O(n*n*k)

Constraints:
1 <= k < 100
1 <= n < 100
0 <= arrij <= 200
'''

#User function Template for python3

class Solution:
    def numberOfPath (self, n, k, arr):
        # code here
        cache={}
        def solve(row,col,k):
            if row>=n or col>=n or k<0:
                return 0
            if k==arr[row][col] and row==n-1 and col==n-1:
                return 1
            if ((row,col),k) in cache:
                return cache[((row,col),k)]
            else:
                cache[((row,col),k)]=solve(row+1,col,k-arr[row][col])+solve(row,col+1,k-arr[row][col])
            return cache[((row,col),k)]
        return solve(0,0,k)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        k= int(input())
        n=int(input())
        l = list(map(int, input().split()))
        arr = list()
        c=0
        for i in range(0, n):
            temp = list()
            for j in range(0, n):
                temp.append(l[c])
                c += 1
            arr.append(temp)
        ans = ob.numberOfPath(n, k, arr);
        print(ans)

# } Driver Code Ends