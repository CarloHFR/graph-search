class Graph:
    def __init__(self):
        self.__edges = []
        self.__vertices = []


    def mostrar(self):
        print(f"V: {self.__vertices}")
        print(f"E: {self.__edges}")


    def __vertice_exists(self, index):
        for vertice in self.__vertices:
            if vertice[0] == index:
                return True
        return False


    def __edge_exists(self, index_vertice1, index_vertice2):
        for edge in self.__edges:
            if edge[0] == index_vertice1 and edge[1] == index_vertice2:
                return True
        return False


    def __get_edge_weight(self, index_vertice1, index_vertice2):
        for edge in self.__edges:
            if edge[0] == index_vertice1 and edge[1] == index_vertice2:
                return edge[2]
        return 0


    def new_vertice(self, index, heuristic):
        if not self.__vertice_exists(index):
            self.__vertices.append([index, heuristic])
            return True
        else:
            return False


    def new_edge(self, index_vertice1, index_vertice2, weight):
        if self.__vertice_exists(index_vertice1) and self.__vertice_exists(index_vertice2) and not self.__edge_exists(index_vertice1, index_vertice2):
            self.__edges.append([index_vertice1, index_vertice2, weight])
            return True
        else:
            return False
