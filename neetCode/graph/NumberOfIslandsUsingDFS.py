

class NumberOfIslandsUsingDFS:
    def numIslands(self, grid: List[List[str]]) -> int:

        # if we have an empty grid, we shall return 0
        if not grid:
            return 0
        # number of rows and number of columns
        rows, cols = len(grid), len(grid[0])
        # to mark cells visited
        visited = set()
        # to count number of islands
        isLands = 0

        # Depth first search method
        def depthFirstSearch(row, col):
            # validation pf whether the landmass is water or land and whether it has been already considered or not.
            if row in range(rows) and col in range(cols) and grid[row][col] == '1' and (row, col) not in visited:
                # add validated coordinates of land unit to the set
                visited.add((row, col))
                # The visited set will include all the coordinates that forms a piece of land using the below recursion.
                # the below recursion will completely stop only when the entire joint land mass is covered for which isLand count will only increase by one.
                depthFirstSearch(row + 1, col)
                depthFirstSearch(row - 1, col)
                depthFirstSearch(row, col + 1)
                depthFirstSearch(row, col - 1)
            # else return to the previous recursive calls.
            else:
                return

        # visit every single position in the grid
        for row in range(rows):
            for col in range(cols):
                #  if we  visit 0 then we don't have to do anything. but if we visit 1 then we have to traverse it and make it visited.
                if grid[row][col] == "1" and (row, col) not in visited:
                    # if we found piece of land then run bredth first search on this cell
                    depthFirstSearch(row, col)
                    #  we are going to increment number of islands only when we make sure that the 1 hasnt already been visited.
                    isLands += 1
        return isLands