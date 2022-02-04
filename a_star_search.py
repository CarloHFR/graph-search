# Código modificado de https://stackabuse.com/basic-ai-concepts-a-search-algorithm/

class AStarSearch:

    def __init__(self):
        pass


    def do_a_star_search(self, graph, start_vertex, end_vertex):
        path = []
        parents = {}
        str_path = " "
        edge_cost = 0
        heuristic_cost = 0
        heuristic_function_cost = 0
        distance_from_start_vertex = {}

        explored_vertices = set([])
        visited_vertices = set([start_vertex])
        
        parents[start_vertex] = start_vertex
        distance_from_start_vertex[start_vertex] = 0

        while len(visited_vertices) > 0:
            current_vertex = None
            
            for visited_vertex in visited_vertices:
                if current_vertex == None or distance_from_start_vertex[visited_vertex] + graph.get_heuristic(visited_vertex) < distance_from_start_vertex[current_vertex] + graph.get_heuristic(current_vertex):
                    current_vertex = visited_vertex

            if current_vertex == None:
                return None

            if current_vertex == end_vertex:
                while parents[current_vertex] != current_vertex:
                    path.append(current_vertex)
                    current_vertex = parents[current_vertex]

                path.append(start_vertex)
                path.reverse()

                prev_vertex = path[0]
                
                for vertex in path:
                    if vertex != prev_vertex:
                        edge_cost += graph.get_weight(prev_vertex, vertex)
                        heuristic_cost += graph.get_heuristic(vertex)
                        heuristic_function_cost += graph.get_weight(prev_vertex, vertex) + graph.get_heuristic(vertex)
                        prev_vertex = vertex

                str_path = " ".join(str(item) for item in path)
                return edge_cost, heuristic_cost, heuristic_function_cost, str_path

            for neighbor in graph.get_neighbors(current_vertex):
                if neighbor not in visited_vertices and neighbor not in explored_vertices:
                    visited_vertices.add(neighbor)
                    parents[neighbor] = current_vertex
                    distance_from_start_vertex[neighbor] = distance_from_start_vertex[current_vertex] + graph.get_weight(current_vertex, neighbor)
                else:
                    if distance_from_start_vertex[neighbor] > distance_from_start_vertex[current_vertex] + graph.get_weight(current_vertex, neighbor):
                        distance_from_start_vertex[neighbor] = distance_from_start_vertex[current_vertex] + graph.get_weight(current_vertex, neighbor)
                        parents[neighbor] = current_vertex

                        if neighbor in explored_vertices:
                            explored_vertices.remove(neighbor)
                            visited_vertices.add(neighbor)

            visited_vertices.remove(current_vertex)
            explored_vertices.add(current_vertex)

        return None
