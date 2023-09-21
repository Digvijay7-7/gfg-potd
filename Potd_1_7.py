#Number of 1 Bits

#User function Template for python3
class Solution:
    def setBits(self, N):
        a = bin(N)[2:]
        count = 0
        for i in a:
            if i == '1':
                count +=1
        return count
        
        '''
        c=0
		while (N>0) :
		    x=N%2
		    N = N//2
		    if x==1 :
		        c +=1
		return c
        '''
        #{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input("Enter number: "))
		ob = Solution()
		ans = ob.setBits(N)
		print('{} times occur 1'.format(ans))

# } Driver Code Ends
'''
def setbits(N):     
    a = bin(N)[2:]
    print(a)
    count = 0
    for i in a:
        if i == '1':
            count = count +1
    print(count)   
setbits(512)
'''