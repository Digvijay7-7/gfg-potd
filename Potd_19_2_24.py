'''
Given a string s of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of k characters. The value of a string is defined as the sum of squares of the count of each distinct character present in the string. 

Example 1:
Input: 
s = abccc, k = 1
Output: 
6
Explaination:
We remove c to get the value as 1^2 + 1^2 + 2^2

Example 2:
Input: 
s = aabcbcbcabcc, k = 3
Output: 
27
Explaination: 
We remove two 'c' and one 'b'. Now we get the value as 3^2 + 3^2 + 3^2.
Your Task:
You do not need to read input or print anything. Your task is to complete the function minValue() which takes s and k as input parameters and returns the minimum possible required value.

Expected Time Complexity: O(n+klog(p))  where n is the length of string and p is number of distinct alphabets and k number of alphabets to be removed. 
Expected Auxiliary Space: O(n)

Constraints:
0 ≤ k ≤ |string length| ≤ 10^5
'''

#User function Template for python3
class Solution:
    def minValue(self, s, k):
        #find frequency of each character and store max Value
        if(len(s)==""):
            return 0
        
        d=dict()
        for char in s:
            if(d.get(char)==None):
                d[char]=1
            else:
                d[char]+=1
        
        #decrease max frequency up to k==0
        while(k!=0):
            maxFreqChar=""
            maxValue=0
            for key,value in d.items():
                if(value>maxValue):
                    maxValue=value
                    maxFreqChar=key
            d[maxFreqChar] -=1
            k-=1
            
        #find ans
        ans=0
        for value in d.values():
            ans += value**2
        
        return ans
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends