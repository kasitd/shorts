def count_islands(graph):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands
    if not graph:
        return 0
    row = len(graph)
    col = len(graph[0])
    count = 0

    for i in range(row):
        for j in range(col):
            if graph[i][j] ==1:
                mark_islands(graph, row, col, i, j)
                count+=1
    return count
    

def mark_islands(graph, row, col, x, y):
    if graph[x][y] == 0:
        return
    graph[x][y]=0

    if x !=0:
        mark_islands(graph, row, col, x-1, y)

    if x !=row-1:
        mark_islands(graph, row, col, x+1, y)

    if y!=0:
        mark_islands(graph, row, col, x, y-1)

    if y !=col -1:
        mark_islands(graph, row, col, x, y+1)


    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.       