'''
Given an array arr[] of length n. Find all possible unique permutations of the array in sorted order. A sequence A is greater than sequence B if there is an index i for which Aj = Bj for all j<i and Ai > Bi.

Example 1:
Input: 
n = 3
arr[] = {1, 2, 1}
Output: 
1 1 2
1 2 1
2 1 1
Explanation:
These are the only possible unique permutations for the given array.

Example 2:
Input: 
n = 2
arr[] = {4, 5}
Output: 
Only possible 2 unique permutations are
4 5
5 4

Your Task:
You don't need to read input or print anything. You only need to complete the function uniquePerms() that takes an integer n, and an array arr of size n as input and returns a sorted list of lists containing all unique permutations of the array.

Expected Time Complexity:  O(n*n!)
Expected Auxilliary Space: O(n*n!)

Constraints:
1 ≤ n ≤ 9
1 ≤ arri ≤ 10
'''

#User function Template for python3
from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        # code here 
        new = permutations(arr)
        unique = set(new)
        a = sorted(list(unique))
        return a
        #return sorted(list(set(permutations(arr,n))))


'''
#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        ans=set()
        def pre(s,i):
            if(i>=len(arr)):
                ans.add(tuple(s))
                return
            for j in range(i,n):
                s[i],s[j]=s[j],s[i]
                pre(s,i+1)
                s[i],s[j]=s[j],s[i]
            
        s=arr
        pre(s,0)
        new=[]
        for i in ans:
            new.append(list(i))
        new.sort()
        return new 
'''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends