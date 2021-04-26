
distances = {'a':{'b':2,'c':1},
'b':{'a':1,'d':1,'c':4},
'c':{'b':5,'d':2,'e':2},
'd':{'c':3,'e':1},
'e':{'c':5}}

distances2 = {'a':{'b':11,'c':2},'b':{'a':3},'c':{'b':5}}

distances3 = {'a':{'c':17,'d':4},'b':{'c':11,'d':8},'c':{'b':5,'a':20},'d':{'b':6,'a':3}}

inf = 999999
def find_path(start,end,network):
    shortest_distances = {}
    previous_nodes = {}    #to determine from which nodes you can reach the given node
    unseen_nodes=network  #sine the algorithm happens multiple time, this is to store unmodified dictionary
    inf = 999999
    path=[]
    #Initially we have to set all to all final distances to infinity except start where it should be 0

    for node in unseen_nodes:
        shortest_distances[node]=inf

    shortest_distances[start] = 0
    #print(shortest_distances)
    while unseen_nodes != {}:
        minNode = None
        for node in unseen_nodes:
            if minNode == None:
                minNode = node
            
            elif shortest_distances[node]<shortest_distances[minNode]:
                minNode = node
            
        
        #print(minNode)
        #print(network[minNode].items())
        
        for connectedNode, weight in network[minNode].items():   #check each connected node to Minnode and its weight (distance)
            
            if (shortest_distances[minNode] + weight) < shortest_distances[connectedNode]:
                shortest_distances[connectedNode] = shortest_distances[minNode]+weight
                #print(connectedNode)
                previous_nodes[connectedNode] = minNode
            
            #print("x")
        #print("1st",shortest_distances)
        unseen_nodes.pop(minNode)
        #print("@@@@@@@@")
        
    #print(shortest_distances)
    print(previous_nodes)
    new = previous_nodes
    path = []
    x=None
    #path.append(start)
    dest = end
    while dest != start:
        try:
            path.append(dest)
            dest = previous_nodes[dest]
        except:
            break
            
    
    
    
    path.append(start)
    path.reverse()
    
    print(path)
    return path
    
        
    
path = find_path('a','e',distances)
print(path)
x=""
for i in path:
    x +=i
print("The fastest path is",x)
#Find previous node of b (c)
#find previous node of c (a) until you reach the start


# a = {1:'a',2:'b'}
# b=a.items()
# print(b)
# for i,j in b:
#      print(i,j)
