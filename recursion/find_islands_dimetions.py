def find_dimetions(map_):
    rows = [i for i, r in enumerate(map_, 1)]
    columns = [x for x, c in enumerate(rows, 1)]
    R = len(rows)
    L = len(columns)
    return(R, L)

def get_others(map_, i, j):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number)

    """
    count = 0
    if (i > 0 and map_[i - 1][j]): 
        count+= 1; 
  
    # LEFT 
    if (j > 0 and map_[i][j - 1]): 
        count+= 1; 
  
    # DOWN 
    if (i < find_dimetions(map_)[0]-1 and map_[i + 1][j]): 
        count+= 1
  
    # RIGHT 
    if (j < find_dimetions(map_)[1]-1 and map_[i][j + 1]): 
        count+= 1; 
  
    return count; 
    
    # your code here
    
    


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0; 
  
    # Traversing the matrix and finding ones to 
    # calculate their contribution. 
    for i in range(0, find_dimetions(map_)[0]): 
        for j in range(0, find_dimetions(map_)[1]): 
            if (map_[i][j]): 
                perimeter += (4 - get_others(map_, i, j)); 
  
    return perimeter