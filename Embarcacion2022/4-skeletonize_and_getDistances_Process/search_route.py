from turtle import distance
import cv2
import sys


sys.setrecursionlimit(10**5)

dc = [-1, -1, -1, 0, 0, 1, 1, 1] #left-top, left, left-bottom, top, bottom, rigth-top, rigth, rigth-bottom
dr = [-1, 0, 1, -1, 1, -1, 0, 1]
w_adjacents = 8.54 # this weight is in meters
w_diag = 12.07
inf = 1e9
weight = [w_diag, w_adjacents, w_diag, w_adjacents, w_adjacents, w_diag, w_adjacents, w_diag]

dataPoints = [
    (1556, 658),
    (1487, 1376),
    (1323, 1693),
    (114, 687),
    (175, 1026),
    (852, 895),
    (514, 1634)
]
adj_list = dict() #adjacency list of the nodes, this is a dict of vectors of tuples (i, j, weight). Where (i, j) is the node


def image_to_graph(nameImg):
    
    img1 = cv2.imread(nameImg)
    rows = len(img1)
    columns = len(img1[0])
    cont_node = 0
    
    for i in range(rows):
        for j in range(columns):
            if(img1[i][j][1] == 255):
                cont_node += 1
                adj_list[(i, j)] = [] #add a empty list where i'll save the adjacency nodes
                for k in range(8):
                    di = i + dr[k] #rows
                    dj = j + dc[k] #columns
                    if(di >= 0 and di < rows and dj >= 0 and dj < columns and img1[di][dj][1] == 255):
                        adj_list[(i, j)].append((di, dj, weight[k])) #here im adding at the node(i,j) in the adj_list a tuple of (di, dj, weight), where di, dj is the row and column of the pixel that is conected with the (i, j)
                        
    return cont_node  

def backtraking(acumulator, current_node):
    
    if(acumulator >= distance_route):
        return True
    
    for edge in adj_list[current_node]:
        to = (edge[0], edge[1]) # To is a tuple of (i, j) where i, j is the row and column of the image
        len = edge[2]
        
        if(nodes_visited[to]):
            continue
        
        nodes_visited[to] = True
        flag = backtraking(acumulator+len, to )
        
        if(flag):
            ri =  to[0]
            ci = to[1]
            out_img[ri][ci] =  [0, 0, 0]
            return True
    
    return False
    
    

def main():
    
    global out_img, nodes_visited, distance_route
    
    #The paths of the images are absolute or from the file path.
    
    print("- Select the option where you want to start the path. The pixel is write as (row, column):")
    for i in range(len(dataPoints)):
        print("     {}. {}".format((i+1), dataPoints[i]))
    print("Select a number: ")
    node_start = dataPoints[int(input())-1] #here you have to put the pixel where you want to start the route (row, column)
    
    print("- Write the distance in meters that you want to transverse :")
    distance_route = (int(input()))/2  #Distance taken to go and the other half to return
    
    print("- Write the path of the superposicionImage (The path of the image are absolute or from the file path.) ")
    image_name = input()  # This is the path of the superposicion image where i read the skeletonize and the complete image
    
    print("Wait a moment, making the process. ")
    
    quantity_nodes = image_to_graph(image_name) 
    
    out_img = cv2.imread(image_name)
    
    print("The process is about to end.")
    
    nodes_visited = dict()
    
    for axis in adj_list:
        nodes_visited[axis] = False
    
    flag_backtrack = backtraking(0, node_start)
    
    if(flag_backtrack):
        out_img[node_start[0]][node_start[1]] = [0, 0, 255] #The start node is color with red, the other path is black
        print("Write the path where you want to save the image and the name.png: ")
        save_path = input()
        cv2.imwrite(save_path, out_img) #Here is the path and name wich you want to named the image to save it
        print("Image saved, where the blacks pixels are the route" )
    else:
        print("Can't find a posible route to the given parameters, please select other ones")
    
main()