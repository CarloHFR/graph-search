from collections import defaultdict


class Graph:
    def __init__(self):
        self.__adjacent_list = defaultdict(set)
        self.__heuristics = {}
        self.__weights = {}


    def is_connected(self, vertex1, vertex2):
        return vertex1 in self.__adjacent_list and vertex2 in self.__adjacent_list[vertex1]

    
    def get_neighbors(self, vertex):
        return self.__adjacent_list[vertex]


    def get_adjacent_list(self):
        return self.__adjacent_list


    def add_vertex(self, vertex1, vertex2):
        self.__adjacent_list[vertex1].add(vertex2)
        self.__adjacent_list[vertex2].add(vertex1)


    def get_heuristic(self, vertex):
        return self.__heuristics[vertex]


    def add_heuristic(self, vertex, heuristic):
        self.__heuristics[vertex] = heuristic


    def get_weight(self, vertex1, vertex2):
        index = f"{vertex1}-{vertex2}"
        if index in self.__weights.keys():
            return self.__weights[index] 

    
    def add_weight(self, vertex1, vertex2, weight):
        if self.is_connected(vertex1, vertex2):
            self.__weights[f"{vertex1}-{vertex2}"] = weight
            self.__weights[f"{vertex2}-{vertex1}"] = weight
