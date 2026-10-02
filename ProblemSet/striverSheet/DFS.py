def dfs(self,v,adj,vis,result):
    # Mark the current node as visited
    vis[v] = True
    # Append the current node to the result list
    result.append(v)
    #Traverse all the neighbors of the current node
    for neighbor in adj[v]:
        # If the neighbor has not been visited, recursively call dfs on it
        if not vis[neighbor]:
            self.dfs(neighbor, adj, vis, result)
def main():
    V = 5  # Number of vertices in the graph
    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]
    # Adding edges to the graph
    adj[0] = [1, 2]
    adj[1] = [0, 3]
    adj[2] = [0, 4]
    adj[3] = [1]
    adj[4] = [2]
    visited = [False] * V  # List to keep track of visited nodes
    result = []  # List to store the result of DFS traversal
    # Perform DFS starting from vertex 0
    dfs(0, adj, visited, result)
    # Print the result of DFS traversal
    print("DFS Traversal:", result)
if __name__ == "__main__":
    main()
