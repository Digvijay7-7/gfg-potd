'''
Given a weighted tree with n nodes and (n-1) edges. You are given q queries. Each query contains a number x. For each query, find the number of paths in which the maximum edge weight is less than or equal to x.

Note: Path from A to B and B to A are considered to be the same.

Example 1:
Input: 
n = 3
edges {start, end, weight} = {{1, 2, 1}, {2, 3, 4}}
q = 1
queries[] = {3}
Output: 
1
Explanation:
Query 1: Path from 1 to 2

Example 2:
Input: 
n = 7
edges {start, end, weight} = {{1, 2, 3}, {2, 3, 1}, {2, 4, 9}, {3, 6, 7}, {3, 5, 8}, {5, 7, 4}}
q = 3
queries[] = {1, 3, 5}
Output: 
1 3 4
Explanation: 
Query 1: Path from 2 to 3
Query 2: Path from 1 to 2, 1 to 3, and 2 to 3
Query 3: Path from 1 to 2, 1 to 3, 2 to 3, and 5 to 7
Your Task:  
You don't need to read input or print anything. Complete the function maximumWeight()which takes integers n, list of edges where each edge is given by {start,end,weight}, an integer q and a list of q queries as input parameters and returns a list of integers denoting the number of possible paths for each query. 

Expected Time Complexity: O(nlogn + qlogn)
Expected Auxiliary Space: O(n)
'''
class Solution:
    def maximumWeight(self, n, edges, q, queries):
        uf = list(range(n))
        sz = [1]*n
        def find(u):
            if uf[u] != u:
                uf[u] = find(uf[u])
            return uf[u]
            
        edges.sort(key=lambda x: x[2], reverse=True)
        queries = sorted(enumerate(queries), key=lambda x:x[1])
        
        res = [0]*q
        cur = 0
        for ind, x in  queries:
            while edges and edges[-1][2] <= x:
                u, v, _ = edges.pop()
                u, v = find(u-1), find(v-1)
                if u != v:
                    uf[u] = v
                    cur += sz[u]* sz[v]
                    sz[v] += sz[u]
            res[ind] = cur
            
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())

        edges = [[0 for j in range(3)] for i in range(n-1)]
        for i in range(n-1):
            input_line = [int(x) for x in input().strip().split()]       
            for j in range (3):
                edges[i][j]=input_line[j]

        q = int(input())
        queries = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.maximumWeight(n, edges, q, queries)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends