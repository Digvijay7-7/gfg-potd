'''
Given an array a of n positive integers. The task is to find the maximum of j - i subjected to the constraint of a[i] < a[j] and i < j.

Example 1:
Input:
n = 2
a[] = {1, 10}
Output:
1
Explanation:
a[0] < a[1] so (j-i) is 1-0 = 1.

Example 2:
Input:
n = 9
a[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output:
6
Explanation:
In the given array a[1] < a[7] satisfying the required condition(a[i] < a[j]) thus giving the maximum difference of j - i which is 6(7-1).
Your Task:
The task is to complete the function maxIndexDiff() which finds and returns maximum index difference. Printing the output will be handled by driver code. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
'''

#User function Template for python3
class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a, n):
        
        l_min,r_max=[a[0]]*n,[a[-1]]*n
        for i in range(1,n):
            l_min[i]=min(l_min[i-1],a[i])
            r_max[-i-1]=max(r_max[-i],a[-i-1])
        l,r,ans=0,0,0
        while l<n and r<n:
            if l_min[l]<=r_max[r]:
                ans=max(ans,r-l)
                r+=1
            else:
                l+=1
        return ans

#{ 
# Driver Code Starts
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))          
            T-=1

if __name__ == "__main__":
    main()
# } Driver Code Ends