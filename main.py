from graph import Graph 
from BFS_search import BFSSearch


def main():
    graph = Graph()

    num_vertex, num_edges = input().split()
    num_vertex = int(num_vertex)
    num_edges = int(num_edges)


    for index in range(1, num_vertex+1):
        heuristic = int(input())
        graph.add_heuristic(index, heuristic)


    for edge in range(1, num_edges+1):
        vertex1, vertex2, weight = input().split()
        vertex1 = int(vertex1)
        vertex2 = int(vertex2)
        weight = int(weight)

        graph.add_vertex(vertex1, vertex2)
        graph.add_weight(vertex1, vertex2, weight)


    start_vertex, end_vertex = input().split()
    start_vertex = int(start_vertex)
    end_vertex = int(end_vertex)

    print("\n\n")

    bfs_search = BFSSearch()
    depth, path_cost, path = bfs_search.do_bfs_search(graph.get_adjacent_list(), start_vertex, end_vertex)

    print(depth)
    print(path_cost)
    print(path)


if __name__ == "__main__":
    main()
