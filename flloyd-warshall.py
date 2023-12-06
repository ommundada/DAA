INF = float('inf')

def cost(i,j,result):
  return result[i][j]

def print_path(i,j,path):
  if path[i][j] is None:
    return [None]
  steps=[j]
  while j!=i:
    j = path[i][j]
    steps.append(j)
  return steps[::-1]

def fw(graph):
  n = len(graph)
  path = [[None]*n for _ in range(n)]
  dist = [[INF]*n for _ in range(n)]
  for i in range(n):
        dist[i][i] = 0
  for i in range(n):
       for j in range(n):
            if i != j and graph[i][j] != 0:
                dist[i][j] = graph[i][j]
                path[i][j] = i
  for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]
  return dist, path


def cost(i,j,result,path):
    print(f"Path from {i} to {j} is:")
    print("===="*5)
    print(f"Path cost: {result[i][j]}")
    for i in range(len(path)-1):
        print(f'{path[i]} → {path[i+1]}. Path cost: {result[path[i]][path[i+1]]}')
    print("\n")

graph = [
    [0,4,3,INF,INF,INF],
    [4,2,INF,2,1,INF],
    [3,INF,0,INF,1,INF],
    [INF,2,INF,0,3,4],
    [INF,1,1,3,4,2],
    [INF,INF,INF,4,2,0]
]
start = 0
end = 5
result, path = fw(graph)
printed_path = print_path(start,end,path)
cost(start,end,result,printed_path)