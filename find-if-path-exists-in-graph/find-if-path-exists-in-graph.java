class Solution {
    public boolean validPath(int n, int[][] edges, int start, int end) {
        Graph g = new Graph(n); 
        
        for (int i = 0; i < edges.length; i++) {
            g.addEdge(edges[i][0], edges[i][1]); 
        }
        
        g.dfs(start); // activate dfs
  
        boolean visited[] = g.visited; 
        return visited[start] && visited[end]; 
    }
}

class Graph {
    public LinkedList<Integer> adjLists[];
    public boolean visited[];
    
    // Graph creation
    Graph(int vertices) {
        adjLists = new LinkedList[vertices];
        visited = new boolean[vertices];

        for (int i = 0; i < vertices; i++)
          adjLists[i] = new LinkedList<Integer>();
      }

    // Add edges, since it's undirected have to add both ways 
    public void addEdge(int src, int dest) {
        adjLists[src].add(dest);
        adjLists[dest].add(src);
    }

    // DFS algorithm
    public void dfs(int vertex) {
        visited[vertex] = true;
        //System.out.print(vertex + " ");

        Iterator<Integer> ite = adjLists[vertex].listIterator();
        while (ite.hasNext()) {
          int adj = ite.next();
          if (!visited[adj])
            dfs(adj);
        }
    }
}