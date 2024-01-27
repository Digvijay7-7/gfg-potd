'''
You are given two four digit prime numbers num1 and num2. Find the distance of the shortest path from Num1 to Num2 that can be attained by altering only single digit at a time such that every number that we get after changing a digit is a four digit prime number with no leading zeros.

Example 1:
Input:
num1 = 1033 
num2 = 8179
Output: 6
Explanation:
1033 -> 1733 -> 3733 -> 3739 -> 3779 -> 8779 -> 8179.
There are only 6 steps reuired to reach num2 from num1. 
and all the intermediate numbers are 4 digit prime numbers.

Example 2:
Input:
num1 = 1033 
num2 = 1033
Output:
0
Your Task:  
You don't need to read input or print anything. Your task is to complete the function solve() which takes two integers num1 and num2 as input parameters and returns the distance of the shortest path from num1 to num2. If it is unreachable then return -1.

Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(n)
'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def solve (self,Num1,Num2):
        #code here
        q = []
        primes = set()
        q.append((Num1, 0))
        primes.add(Num1)
        
        while q:
            cur, level = q.pop(0)
            if cur == Num2:
                return level
                
            for i in range(4):
                for d in range(10):
                    newNum = cur
                    if i == 0 and d == 0:
                        continue
                    
                    newNum = int(str(cur)[:i] + str(d) + str(cur)[i+1:])
                    if newNum not in primes and self.isPrime(newNum):
                        q.append((newNum, level+1))
                        primes.add(newNum)
        return -1
        
    def isPrime(self, n):
        if n < 2:
            return 0
        for i in range(2, int(n**0.5)+1):
            if n%i== 0:
                return 0
        
        return 1



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1,num2=map(int,input().split())
        ob = Solution()
        print(ob.solve(num1,num2))
# } Driver Code Ends