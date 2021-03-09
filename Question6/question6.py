# Define Infinite
INT_MAX = 10000

def ccw(A,B,C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0]) 

#return if the line AB CD intersect
def ifintersect(A,B,C,D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# Returns true if the point p lies inside the polygon[] with n vertices 
def ifinsidepolygon(ptpolygon, pt):
     
    n = len(ptpolygon)
         
    # Create a point for horizontal line segment from p-infinite
    inf = (INT_MAX, pt[1])
    count = i = 0
     
    while True:
        next = (i + 1) % n 
        # Check if line segment p-inf intersects with the line polygon[i]-polygon[next]
        if (ifintersect(ptpolygon[i], ptpolygon[next], pt, inf)):                             
            count += 1     
        i = next
        if (i == 0):
            break
    # Return true if count is odd, false otherwise 
    return (count % 2 == 1)
 
# main function
if __name__ == '__main__':
     
    polygon = [ (4, 3),(2, 6),(3, 12),(2, 17),(5, 20),(9, 21),(14, 19),(20, 14),(18, 3),(11, 7)]       
    p = [(7, 11),(10,14),(11,4),(12,21),(16,3),(16,10),(17,4),(18,7),(18,17),(20,7)]
     
    #Output the result
    for data in p:
        if (ifinsidepolygon(polygon, data)):
            print(data[0],data[1], 'Inside')
        else:
            print(data[0],data[1],'Outside')
