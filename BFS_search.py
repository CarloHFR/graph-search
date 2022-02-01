# Código modificado de https://stackabuse.com/graphs-in-python-breadth-first-search-bfs-algorithm/

from queue import Queue

class BFSSearch:

    def __init__(self):
        pass


    def do_bfs_search(self, adjacent_list, start_vertex, end_vertex):
        visited = set()
        queue = Queue()
        parent = dict()

        path = []
        depth = 0
        str_path = ""
        path_cost = 0
        path_found = False

        queue.put(start_vertex)
        visited.add(start_vertex)
        parent[start_vertex] = None

        while not queue.empty():
            current_vertex = queue.get()
            if current_vertex == end_vertex:
                path_found = True
                break

            for next_vertex in adjacent_list[current_vertex]:
                if next_vertex not in visited:
                    queue.put(next_vertex)
                    parent[next_vertex] = current_vertex
                    visited.add(next_vertex)

        if path_found:
            path.append(end_vertex)
            while parent[end_vertex] is not None:
                path.append(parent[end_vertex]) 
                end_vertex = parent[end_vertex]
                depth += 1
                path_cost += 1
            path.reverse()
            str_path = " ".join(str(item) for item in path)

        return depth, path_cost, str_path
