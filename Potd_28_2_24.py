'''
Given a string representation of a decimal number s, check whether it is divisible by 8.

Example 1:

Input:
s = "16"
Output:
1
Explanation:
The given number is divisible by 8,
so the driver code prints 1 as the output.
Example 2:

Input:
s = "54141111648421214584416464555"
Output:
-1
Explanation:
Given Number is not divisible by 8, 
so the driver code prints -1 as the output.
Your Task:
You don't need to read input or print anything.Your task is to complete the function DivisibleByEight() which takes a string s as the input and returns 1 if the number is divisible by 8, else it returns -1.

Expected Time Complexity: O(1).
Expected Auxillary Space: O(1).
'''

#User function Template for python3

class Solution:
    def DivisibleByEight(self, s):
        n = len(s)
        
        # If the number has at most three digits, we can directly check
        if n <= 3:
            num = int(s)
            if num % 8 == 0:
                return 1
            else:
                return -1
        
        # Otherwise, check if the last three digits form a multiple of 8
        num = int(s[-3:])
        if num % 8 == 0:
            return 1
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends