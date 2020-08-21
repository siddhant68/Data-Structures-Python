class Graph:
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        
    def bfs(self, source):
        visited = [False] * len(self.graph)
        queue = [source]
        visited[source] = True
        while len(queue) > 0:
            ele = queue.pop(0)
            print(ele, end=' ')
            
            
            for i in self.graph[ele]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
    
    def dfs(self, source):
        visited = [False] * len(self.graph)
        visited[source] = True
        dfsRec(source, visited)
        
    def dfsRec(self, vertex, visited):
        print(vertex, end=' ')
        visited[vertex] = True
        
        for i in self.graph[vertex]:
            if not visited[i]:
                dfsRec(i, visited)
                visited[i] = True
            

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

print(g.graph)
g.bfs(2)
print()
g.dfs(source)