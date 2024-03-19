'''
Given a square matrix a of size n x n, where each cell can be either 'X' or 'O', you need to find the size of the largest square subgrid that is completely surrounded by 'X'. More formally you need to find the largest square within the grid where all its border cells are 'X'.

Example 1:
Input:
n = 2
a = [[X,X],
     [X,X]]
Output:
2
Explanation:
The largest square submatrix surrounded by X is the whole input matrix.

Example 2:
Input:
n = 4
a = [[X,X,X,O],
     [X,O,X,X],
     [X,X,X,O],
     [X,O,X,X]]
Output:
3
Explanation:
Here,the input represents following matrix of size 4 x 4
X X X O
X O X X
X X X O
X O X X
The square submatrix starting at 
(0,0) and ending at (2,2) is the 
largest submatrix surrounded by X.
Therefore, size of that matrix would be 3.
Your Task:
You don't need to read input or print anything. Your task is to complete the function largestSubsquare() which takes the integer n and the matrix a as input parameters and returns the size of the largest subsquare surrounded by 'X'.

Expected Time Complexity: O(n^2)
Expected Auxillary Space: O(n^2)
'''

#User function Template for python3

class Solution:
    def largestSubsquare(self, n, a):
        row_by=[[0]*n for _ in range(n)]
        col_by=[[0]*n for _ in range(n)]
        for i in range(n):
            row=0
            col=0
            for j in range(n):
                if a[i][j]=="X":
                    row+=1
                else:
                    row=0
                row_by[i][j]=row
                if a[j][i]=="X":
                    col+=1
                else:
                    col=0
                col_by[j][i]=col
        res=0
        for i in range(n):
            for j in range(n):
                side=min(row_by[i][j],col_by[i][j])
                while side>res:
                    if row_by[i-side+1][j]>=side and col_by[i][j-side+1]>=side:
                        res=side
                    else:
                        side-=1
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[]
        for i in range(n):
            s=list(map(str,input().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.largestSubsquare(n,a))
# } Driver Code Ends