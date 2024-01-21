'''
Vertex cover of an undirected graph is a list of vertices such that every vertex not in the vertex cover shares their every edge with the vertices in the vertex cover. In other words, for every edge in the graph, atleast one of the endpoints of the graph should belong to the vertex cover. You will be given an undirected graph G, and your task is to determine the smallest possible size of a vertex cover.

Example 1:
Input:
N=5
M=6
edges[][]={{1,2}
           {4, 1},
           {2, 4},
           {3, 4},
           {5, 2},
           {1, 3}}
Output:
3
Explanation:
{2, 3, 4} forms a vertex cover
with the smallest size.

Example 2:
Input:
N=2
M=1
edges[][]={{1,2}} 
Output: 
1 
Explanation: 
Include either node 1 or node 2
in the vertex cover.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function vertexCover() which takes the edge list and an integer n for the number of nodes of the graph as input parameters and returns the size of the smallest possible vertex cover.

Expected Time Complexity: O(M*N2log(N))
Expected Auxiliary Space: O(N2)
'''

'''
from typing import List
from itertools import combinations
class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        nodes = list(range(1, n+1))
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo)//2
            for perm in combinations(nodes, mid):
                perm = set(perm)
                if all(u in perm or v in perm for u, v in edges):
                    hi = mid
                    break
            else:
                lo = mid + 1
        return lo
'''

from typing import List

class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        def solve(edges):
            if len(edges)==0:
                return 0
            ed0=[]
            ed1=[]
            for i in edges:
                if not(i[0]==edges[0][0] or i[1]==edges[0][0]):
                    ed0.append(i)
                if not(i[0]==edges[0][1] or i[1]==edges[0][1]):
                    ed1.append(i)
            ans0=1+solve(ed0)
            ans1=1+solve(ed1)
            return min(ans0,ans1)            
        return solve(edges)

#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        
        edges=IntMatrix().Input(m, m)
        
        obj = Solution()
        res = obj.vertexCover(n, edges)
        
        print(res)
        

# } Driver Code Ends