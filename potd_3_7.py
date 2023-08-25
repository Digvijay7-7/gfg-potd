class Solution:
    def maxIndexDiff(self,arr,n):
        lMin=[arr[0]]*n
        rMax=[arr[n-1]]*n
           
        for i in range(1, n):
            lMin[i]=min(arr[i], lMin[i-1])
        
        for i in range(n-2, -1, -1):
            rMax[i]=max(arr[i], rMax[i+1])
        
        i, j, ans=0, 0, -1
        while i<n and j<n:
            if lMin[i]<=rMax[j]:
                ans=max(j-i, ans)
                j+=1
            else:
                i+=1
        return ans
#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends