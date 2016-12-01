import heapq

## Had to change the graph from dictionary list to dictionary dictionary
## Allowed me to add the weight values 

class Node(object):
    def __init__(self,node):
        self.id = node
        self.adjacent = {}
        
    def __lt__(self,other):
        return self.id < other.id

    def get_id(self):
        return self.id

    def add_neighbour(self,neighbour,weight=0):
        self.adjacent[neighbour] = weight
  
    def __str__(self):
        return str(self.id) + ': ' + str([x.id for x in self.adjacent])
    
    def get_weight(self, neighbour):
        return self.adjacent[neighbour]
    
    def get_connections(self):
        return self.adjacent.keys()

class Graph(object):
    def __init__(self):
        self.node_dict = {}

    def __iter__(self):
        return iter(self.node_dict.values())


    def add_node(self,node):
        new_node = Node(node)
        self.node_dict[node] = new_node
        return new_node

    def get_node(self,n):
        if n in self.node_dict:
            return self.node_dict[n]
        else:
            return None
    def add_edge(self,frm,to,weight=0):
        if frm not in self.node_dict:
            self.add_node(frm)
        if to not in self.node_dict:
            self.add_node(to)
        self.node_dict[frm].add_neighbour(self.node_dict[to],weight)
        self.node_dict[to].add_neighbour(self.node_dict[frm],weight)

    def get_nodes(self):
        return self.node_dict.keys()
    


def Dijkstra(graph, start, end):
    queue,seen = [(0, start, [])],set()
    while True:
        try:
            (cost,v,path) = heapq.heappop(queue)
        except IndexError:
            #print('NO CONNECTION')
            return ('NA', None)
        
        v = str(v)
        v = v[0]

        if v not in seen:
            path = path + [v]
            seen.add(v)
            if v == end:
                return cost, path
            for next in set(graph[v].adjacent):
                c = graph[v].get_weight(next)
                heapq.heappush(queue, (cost + c, next, path))
                

if __name__ == '__main__':
    g = Graph()

    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')
    g.add_node('g')
    g.add_node('h')
    g.add_node('i')
    g.add_node('j')
        
    g.add_edge('a','h',14)
    g.add_edge('a','c',7)
    g.add_edge('a','f',9)
    g.add_edge('b','h',9)
    g.add_edge('b','z',6)
    g.add_edge('h','f',2)
    g.add_edge('c','f',10)
    g.add_edge('c','z',11)
    
    
    print('All of the nodes in the graph:')
    print(g.get_nodes(),'\n')
    
    print('Graph Layout')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('Node:',vid,'->',wid,'Cost:',v.get_weight(w))

    

    cost, path = Dijkstra(g.node_dict,'a','b')#Using a,b in this example
    print("\nDijkstra's shortest path:")
    print('Path:',path,'Cost:',cost)
    
