
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        arr = [x for x in range(len(edges)+1)]
        def find(x):
            if arr[x] == x:
                return x
            return find(arr[x])
        def union(a, b):
            arr[find(a)] = b
        for a, b in edges:
            if find(a) == find(b):
                return [a, b]        
            union(a, b)
