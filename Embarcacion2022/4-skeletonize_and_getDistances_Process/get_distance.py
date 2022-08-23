#En este archivo se deben hacer algunos cambios para que funcione
# 1.     	image_name = "image_name.png"
# 2. nodeStart = (row, column)
#	 nodeFinal = (row, column)
# 3. cv2.imwrite('imageName_to_save.png', img1) 


from queue import PriorityQueue
import cv2

dc = [-1, -1, -1, 0, 0, 1, 1, 1] #left-top, left, left-bottom, top, bottom, rigth-top, rigth, rigth-bottom
dr = [-1, 0, 1, -1, 1, -1, 0, 1]
w_adjacents = 8.54 # this weight is in meters
w_diag = 12.07
inf = 1e9
weight = [w_diag, w_adjacents, w_diag, w_adjacents, w_adjacents, w_diag, w_adjacents, w_diag]

adj_list = dict() #adjacency list of the nodes, this is a dict of vectors of tuples (i, j, weight). Where (i, j) is the node



def image_to_graph(nameImg):
    
    img1 = cv2.imread(nameImg)
    rows = len(img1)
    columns = len(img1[0])
    cont_node = 0
    
    # print (get_node)        
    # print ("_______________")
    for i in range(rows):
        for j in range(columns):
            if(img1[i][j][1] == 255):
                cont_node += 1
                adj_list[(i, j)] = [] #add a empty list where i'll save the adjacency nodes
                for k in range(8):
                    di = i + dr[k]
                    dj = j + dc[k]
                    if(img1[di][dj][1] == 255):
                        adj_list[(i, j)].append((di, dj, weight[k])) #here im adding at the node(i,j) in the adj_list a tuple of (di, dj, weight), where di, dj is the row and column of the pixel that is conected with the (i, j)
                        
    # print(adj_list)
    return cont_node              


def restore_path(start, final, parent):
    path = []
    v = final
    while(v != start):
        path.append(v)
        v = parent[v]
    path.append(start)
    
    return path
    
#This is the clasical diijkstra algorithm
def dijkstra(root, distances, p):
    
    distances[root] = 0
    
    pq = PriorityQueue()
    pq.put((0, root))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        
        if(dist != distances[current_vertex]):
            continue
        
        for edge in adj_list[current_vertex]:
            to = (edge[0], edge[1])
            len = edge[2]
            
            if(distances[current_vertex] + len < distances[to]):
                distances[to] = distances[current_vertex] + len
                p[to] = current_vertex
                pq.put((distances[to], to))

def main():
    
    image_name = "./MetodologiaEjemplos/skMetodologia.png"  # This is the path where the skeletonize image is saved
    quantity_nodes = image_to_graph(image_name)
    
    nodeStart = (258, 1650) #here you have to put the pixel where you want to start the graph (row, column)
    nodeFinal = (1819, 251) #here you have to put the pixel where you want to reach
    
    # print(nodeStart, nodeFinal)
    
    parent = dict()
    distances = dict() 
    
    for axis in adj_list:
        parent[axis] = -1
        distances[axis] = inf # initialize distance list as all infinities
    
    dijkstra(nodeStart, distances, parent)
    # print("__________________")
    path = restore_path(nodeStart, nodeFinal, parent)
    # print("__________________")
    # print(distances)
    
    img1 = cv2.imread(image_name)
    
    for i in path:
        ri =  i[0]
        ci = i[1]
        img1[ri][ci] =  [0, 0, 255]
        
    print("distances in meters: ", distances[nodeFinal])
    cv2.imwrite('./MetodologiaEjemplos/distance.png', img1) #Here is the path and name wich you want to named the image
    
    
main()


