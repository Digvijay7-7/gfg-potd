'''
It is a universal fact that Geekina hates 1s however it is also known that Geekina loves the integers having atmost k 1s (set-bits) in their binary representation. 

Geekina demanded nth such non-negative number from Geek, and being a good friend of Geek, now it's your responsibility to tell him that number.

Note: The test cases are generated such that the answer always exists and will fit in the 64-bit data type.

Example 1:
Input:
n = 5
k = 1
Output:
8
Explanation:
Following numbers are loved by Geekina -
0 = (0)^2
1 = (1)^2
2 = (10)^2
4 = (100)^2
8 = (1000)^2

Example 2:
Input:
n = 6
k = 2
Output:
5
Explanation:
Following numbers are loved by Geekina -
0 = (0)^2
1 = (1)^2
2 = (10)^2
3 = (11)^2
4 = (100)^2
5 = (101)^2

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function findNthNumer() that takes n and k as input parameters. Return the nth number having at most k set-bits.

Expected Time Complexity: O(k*log(n) + constant)
Expected Auxiliary Space: O(k*log(n) + constant)

Constraints:
1 <= n <= 10^9
1 <= k <= 63
'''

from typing import List
from math import log2, factorial

class Solution:
    def comb(self, n, r):
        return factorial(n)//(factorial(r) * factorial(n-r)) if n >= r else 0
        
    def count_exact(self, a, k):
        if k == 0:
            return 1
        if a == 0:
            return 0
        m = int(log2(a))
        if m < k-1:
            return 0
        return self.comb(m, k) + self.count_exact(a^(1<<m), k-1)
        
    def count(self, a, k):
        return sum(self.count_exact(a, i) for i in range(k+1))
        
    def findNthNumber(self, n : int, k : int ) -> int:
        lo, hi = 0, 10**18
        while lo < hi:
            mid = lo + (hi - lo)//2
            if self.count(mid, k) >= n:
                hi = mid 
            else:
                lo = mid + 1
        return lo

#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k=map(int,input().split())
        
        obj = Solution()
        res = obj.findNthNumber(n,k)
        
        print(res)
        
# } Driver Code Ends