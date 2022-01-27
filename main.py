from graph import Graph 


def main():
    graph = Graph()

    num_vertices, num_edges = input().split()
    num_vertices = int(num_vertices)
    num_edges = int(num_edges)

    for index in range(1, num_vertices+1):
        heuristic = int(input())
        graph.new_vertice(index, heuristic)

    for edge in range(1, num_edges+1):
        index_vertice1, index_vertice2, weight = input().split()
        index_vertice1 = int(index_vertice1)
        index_vertice2 = int(index_vertice2)
        weight = int(weight)
        graph.new_edge(index_vertice1, index_vertice2, weight)

    start_vertice, end_vertice = input().split()
    start_vertice = int(start_vertice)
    end_vertice = int(end_vertice)

    graph.mostrar()


if __name__ == "__main__":
    main()