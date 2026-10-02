class Solution:
    def dfs(self,node,adj,vis):
    # Mark the current node as visited
        vis[node] = True
    # Traverse all the neighbors of the current node
        for neighbor in adj[node]:
        # If the neighbor has not been visited, recursively call dfs on it
            if not vis[neighbor]:
                self.dfs(neighbor, adj, vis)
    def numProvinces(self, adj, V):
        adj_list = [[] for _ in range(V)]  # Create an adjacency list
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:  # If there is an edge between i and j
                    adj_list[i].append(j)  # Add j to the adjacency list of i
                    adj_list[j].append(i)  # Add i to the adjacency list of j (undirected graph)
        visited = [False] * V  # List to keep track of visited nodes
        count = 0  # Initialize province count
        for i in range(V):
            if not visited[i]:  # If the node has not been visited
                count += 1  # Increment the province count
                self.dfs(i, adj_list, visited)  # Perform DFS starting from the unvisited node
        return count
if __name__ == "__main__":
    # Example usage
    adj = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]  # Adjacency matrix representation of the graph
    V = len(adj)  # Number of vertices in the graph  # Create an instance of the Solution class
    solution = Solution()
    print("Number of Provinces:", solution.numProvinces(adj, V))  # Print the number of provinces