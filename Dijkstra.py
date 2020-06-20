def dijkstra(graph, src, end):
    if graph == None:
        return None
    












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