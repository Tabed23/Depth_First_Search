class Graph:

    def __init__(self):
        # make private instances
        print("Graph Constructor has been called\n")
        self.__frontier = []  # list
        self.__visited = []  # list
        self.__graph = {}  # dictionary
        self.__parent = {}  # dictionary

    def get_frontier(self):  # get the frontier
        return self.__frontier

    def get_visited(self):  # get visited
        return self.__visited

    def __push_node(self, node):  # push the node in the queue
        self.__frontier.append(node)

    def __pop_node(self):   # pop the node from queue
        return self.__frontier.pop()

    def set_graph(self, g):  # set the graph
        self.__graph = g

    def get_graph(self):  # get the graph
        return self.__graph

    def print_graph(self):  # print the graph
        print(self.__graph)

    # Path to goal finder
    def path_to_goal(self, start_node, end_node):
        path = [end_node]
        while path[-1] != start_node:
            path.append(self.__parent[path[-1]])
        path.reverse()
        return path

    def DFS(self, start_state, goal_state):  # depth first search
        self.__push_node(start_state)
        while len(self.__frontier) != 0:
            node = self.__pop_node()
            if node not in self.__visited:
                self.__visited.append(node)
            for nodes in reversed(self.__graph[node]):
                if nodes not in self.__visited:
                    self.__parent[nodes] = node
                    self.__push_node(nodes)
            if goal_state == node:
                print("found")

        return self.__visited
