'''
Consider the generalized Fibonacci number g, which is dependent on a, b and c as follows :-
g(1) = 1, g(2) = 1. For any other number n, g(n) = a*g(n-1) + b*g(n-2) + c.

For a given value of m, determine g(n)%m.

Example 1:
Input:
a = 3
b = 3
c = 3
n = 3
m = 5
Output:
4
Explanation:
g(1) = 1 and g(2) = 1 
g(3) = 3*g(2) + 3*g(1) + 3 = 3*1 + 3*1 + 3 = 9
We need to return answer modulo 5, so 9%5 = 4, is the answer.

Example 2:
Input:
a = 2
b = 2
c = 2
n = 4
m = 100
Output:
16
Explanation:
g(1) = 1 and g(2) = 1
g(3) = 2*g(2) + 2*g(1) + 2 = 2*1 + 2*1 + 2 = 6
g(4) = 2*g(3) + 2*g(2) + 2  = 2*6 + 2*1 + 2 = 16
We need to return answer modulo 100, so 16%100 = 16, is the answer.
Your Task:
You don't need to read input or print anything. Your task is to complete the function genFibNum() which takes 5 Integers a, b, c, n, and m as input and returns g(n)%m.

Expected Time Complexity: O( log(n) ).
Expected Auxiliary Space: O(1).
'''

#User function Template for python3

class Solution:
    def mult(self, mat1, mat2, m):
        mat = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    mat[i][j] += mat1[i][k] * mat2[k][j]
                mat[i][j] %= m
        return mat
     
    def exp(self, mat, n, m):
        if n == 0:
            return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        elif n == 1:
            return mat
        else:
            math = self.exp(mat, n//2, m)
            matf = self.mult(math, math, m)
            if n%2:
                matf = self.mult(matf, mat, m)
            return matf
            
    def genFibNum(self, a, b, c, n, m):
        if n <= 2:
            return 1%m
        else:
            return sum(self.exp([[a, b, c], [1, 0, 0], [0, 0, 1]], n-2, m)[0])%m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b,c,n,m=map(int,input().split())
        
        ob = Solution()
        print(ob.genFibNum(a,b,c,n,m))
# } Driver Code Ends