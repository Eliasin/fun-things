#Recursive depth first search
#No negative weights
def dfs(adjacency, current, goal):
  def _dfs(adjacency, visited, current, goal):
    if (current == goal):
      return True
    for to in range(len(adjacency)):
      if (adjacency[current][to] != -1 and to not in visited):
        visited.append(to)
        _dfs(adjacency, visited, to, goal)
        
  visited = []
  _dfs(adjacency, visited, current, goal)
  return goal in visited
  
#Represents a graph with 4 nodes, 0 - 3 where 0 and 1 are connected to 2 but nothing is connected to 3 
adjacency = [[0, -1, 1, -1], [-1, 0, 1, -1], [1, 1, 0, -1], [-1, -1, -1, 0]]

#Can you reach 1 from 0?
print(dfs(adjacency, 0, 1))

#Can you reach 3 from 0?
print(dfs(adjacency, 0, 3))
