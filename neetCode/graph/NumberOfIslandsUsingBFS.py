# Using Bredth first search
import collections


class NumberOfIslandsUsingBFS:
    def numIslands(self, grid: List[List[str]]) -> int:

        # if we have an empty grid, we shall return 0
        if not grid:
            return 0
        # number of rows and number of colums
        rows, cols = len(grid), len(grid[0])
        # to mark cells visited
        visited= set()
        # to count number of islands
        isLands=0


        # Bredth first search method
        def breadthFirstSerch(row, col):
            #  as bredth first search is not a recursive algorithm, its iterative, we will need queue datastructure
            queue=collections.deque()
            # we add coordinated to visited
            visited.add((row,col))
            # also we append the coordintates to the queue
            queue.append((row,col))

            # while queue is not empty
            while queue:
                # pop the last coordinate in queue (new elements are added to the right hence the old coordinates will be popped from left.)
                poppedRow, poppedCol=queue.popleft()
                # all four directions of the unit length up down left and right
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                # for all four directions
                for horizontal, vertical in directions:
                    # now variable row and col will have new coordinates of each unit directions
                    row, col=poppedRow+horizontal, poppedCol+vertical
                    # if row is not out of range and column is not out of range and the coordinate is land and the coordinates arent already visited
                    if row in range(rows) and col in range(cols) and grid[row][col]=='1' and (row,col) not in visited:
                        # then add it to the queue
                        queue.append((row, col))
                        # add it to visited set
                        visited.add((row,col))





        # visit every single position in the grid
        for r in range(rows):
            for c in range(cols):
                #  if we  visit 0 then we don't have to do anything. but if we visit 1 then we have to traverse it and make it visited.
                if grid[r][c]=="1" and (r,c) not in visited:
                    # if we found piece of land then run bredth first search on this cell
                    breadthFirstSerch(r,c)
                    #  we are going to increment number of islands only when we make sure that the 1 hasnt already been visited.
                    isLands+=1
        return isLands

