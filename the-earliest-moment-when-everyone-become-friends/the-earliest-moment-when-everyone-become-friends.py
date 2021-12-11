class Solution(object):
    
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """ 
        # Sort the logs by time 
        logs.sort(key=lambda x: x[0], reverse=False)
        
        uf = UnionFind(n); 
        
        # now we try connect 
        for i in range (len(logs)):
            uf.union(logs[i][1], logs[i][2])
            # check the connectedness 
            noOfDisjoin = uf.getNoOfRoot()
            if (noOfDisjoin == 1):
                return logs[i][0]
        return -1 
            
    
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def getNoOfRoot(self):
        count = 0
        for i in range(len(self.root)):
            if self.root[i] == i:
                count += 1
        return count 

        