
class Node(object):
        def __init__(self,node,lis=[]):
                self.id = node
                self.adjacent = []

        def get_id(self):
                return self.id
        
        def add_neighbour(self,neighbour):
                self.adjacent.append(neighbour)
                return self.adjacent

        def __repr__(self):
                return "Node(%s = %s)"%(str(self.id),str(self.adjacent))
        def __str__(self):
                return self.__repr__()

class Graph(object):
        def __init__(self):
                self.node_dict = {}

        def __iter__(self):
                return iter(self.node_dict.values())

        def add_node(self,node):
                new_node = Node(node)
                self.node_dict[node] = new_node
                return new_node

        def get_node(self, n):
                if n in self.node_dict:
                        return self.node_dict[n]
                else:
                        return None

        def add_edge(self,frm,to):
                if frm not in self.node_dict:
                        self.add_node(frm)
                if to not in self.node_dict:
                        self.add_node(to)
                self.node_dict[frm].add_neighbour(to)
                self.node_dict[to].add_neighbour(frm)
        def get_nodes(self):
                return self.node_dict.keys()
#TASK 14 here

def DFS(graph,start):
        visited, stack = [], [start]
        while stack: #something is in stack run
                edge = stack.pop()#Removes item at end of list
                if edge not in visited:
                        visited.append(edge)
                        stack.extend(set(graph[edge].adjacent) - set(visited))
                        #extend the stack by appending all the items in the list
                        #without all the already visited nodes
        text_writer('DFS tranverse.txt',start,visited)
        return visited

def BFS(graph,start):
        visited, queue = [],[start]
        while queue:
                edge = queue.pop(0)#takes from the front
                if edge not in visited:
                        visited.append(edge)
                        queue.extend(set(graph[edge].adjacent) - set(visited))
        text_writer('BFS tranverse.txt',start,visited)
        return visited
        
def text_writer(name,start,result):
        f = open(name,"a")
        f.write("\n")
        f.write(start)
        f.write(" = ")
        f.write(str(result))
        f.close()
#END OF TASK 14

if __name__ == '__main__':
        g = Graph()

        g.add_node('a')
        g.add_node('b')
        g.add_node('c')
        g.add_node('d')
        g.add_node('e')
        g.add_node('f')
        
        #If the node doesn't already exist it will be made
        g.add_edge('a','b')
        g.add_edge('a','s')
        g.add_edge('s','c')
        g.add_edge('s','g')
        g.add_edge('c','d')
        g.add_edge('c','f')
        g.add_edge('c','e')
        g.add_edge('g','f')
        g.add_edge('g','h')
        g.add_edge('h','e')
        g.add_edge('h','p')


        #print('NODE IS:', g.get_node('a'))
        print('The following is all of the nodes in the graph:')
        print(g.get_nodes(),'\n')
        print('What each node is connected to:')

        for w in g.node_dict:
                print(g.get_node(w))

        #THIS SECTION IS PART OF TASK 14
        #Used starting node for example
        print('\nDFS tranverse: ',DFS(g.node_dict,'a'))
        print('BFS tranverse:',BFS(g.node_dict,'a'))
        
                        

