def dijkstra(graph, src, dst):
    if graph == None:
        return None
    nodes = [i for i in range(len(graph))]
    dist = [float('inf')]*len(graph)
    dist[src] = 0
    dist_init = [i for i in graph[src]]
    path = []
    #path.append(src)
    visited = []
    visited.append(src)
    while nodes:
        nextVertexDist = min([vDist for vertex,vDist in enumerate(dist_init) if vertex in nodes])
        nextVertex = dist_init.index(nextVertexDist)
        path.append(nextVertex)
        nodes.remove(nextVertex)
        for vertex,vDist in enumerate(graph[nextVertex]):
            if 0<vDist<inf:
                if dist[vertex] > dist[nextVertex]+vDist:
                    dist[vertex] = dist[nextVertex]+vDist
                    dist_init[vertex] = dist[vertex]
    return path,dist

if __name__ == '__main__':
    # graph 图的邻接矩阵
    inf = float('inf')
    graph = [
        [0.0, 2.0, 8.0, 1.0, inf, inf, inf, inf],
        [2.0, 0.0, 6.0, inf, 1.0, inf, inf, inf],
        [9.0, 6.0, 0.0, 7.0, 4.0, 2.0, 2.0, inf],
        [1.0, inf, 7.0, 0.0, inf, inf, 9.0, inf],
        [0.0, 1.0, 4.0, inf, 0.0, 3.0, inf, 9.0],
        [inf, inf, 2.0, inf, 3.0, 0.0, 4.0, 6.0],
        [inf, inf, 2.0, 9.0, inf, 4.0, 0.0, 2.0],
        [inf, inf, inf, inf, 9.0, 6.0, 2.0, 0.0]
    ]
    path,distance = dijkstra(graph,0,7)
    print(path)
    print(distance)