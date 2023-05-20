class Solution {
    
    List<Integer> children_nodes = new ArrayList<>(); 
    
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        
        UnionFind uf = new UnionFind(n); 
        for (int i = 0; i < edges.length; i++) {
            uf.union(edges[i][0], edges[i][1]);
        }
        
        // count number of root nodes
        int count = 0; 
        for (int i = 0; i < uf.root.length; i++) {
            if (uf.root[i] == i) {
                count += 1; 
            }
        }        
        System.out.println(Arrays.toString(uf.root));
        return count == 1? true : false; 
    }
}


public class UnionFind {
    public int[] root;
    public int[] rank; 

    public UnionFind(int size) {
        root = new int[size];
        rank = new int[size];
        for (int i = 0; i < size; i++) {
            root[i] = i;
            rank[i] = i; 
        }
    }
    
    public int find(int x) {
        if (x == root[x]) {
            return x;
        }
        return root[x] = find(root[x]);
    }
    
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                root[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                root[rootX] = rootY;
            } else {
                root[rootY] = rootX;
                rank[rootX] += 1;
            }
        }
    }
}
