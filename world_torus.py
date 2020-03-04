from world import World

class World_Torus(World):
    def create_neighbors(self):
        """
        Using a loop create each cell's neighbors
        and a append it to a list
        :param: none
        :return: none
        """
        for row in self._currentGrid:
            for cell in row:
                row = cell.get_row()
                column = cell.get_column()
                if row == 0:
                    # 1. upper left corner (3 neighbors)
                    if column == 0:
                        #print('upper left')
                        cell.add_neighbor(self._currentGrid[row][self._columns - 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row + 1][self._columns - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row + 1][column + 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[self._rows - 1][column])
                        cell.add_neighbor(self._currentGrid[self._rows - 1][column + 1])
                    # 2. rest of the top row (5 neighbors)
                    elif column < (self._columns - 1):
                        #print('upper')
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row + 1][column + 1])
                        cell.add_neighbor(self._currentGrid[self._rows - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[self._rows - 1][column])
                        cell.add_neighbor(self._currentGrid[self._rows - 1][column + 1])
                    # upper right corner (3 neighbors)
                    else:
                        #print('upper right')
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row][column - self._columns - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column - self._columns - 1])
                        cell.add_neighbor(self._currentGrid[self._rows - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[self._rows - 1][column])
                # middle row
                elif row < (self._rows - 1):
                    #print('middle')
                    # 1. middle left edge (5 neighbors)
                    if column == 0:
                        #print('middle left edge')
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row - 1][column + 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row + 1][column + 1])
                        cell.add_neighbor(self._currentGrid[row - 1][self._columns - 1])
                        cell.add_neighbor(self._currentGrid[row][self._columns - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][self._columns - 1])
                    # 2. rest of the middle row (8 neighbors)
                    elif column < (self._columns - 1):
                        #print('upper')
                        cell.add_neighbor(self._currentGrid[row - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row - 1][column + 1])
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row + 1][column + 1])
                    # 3. middle right edge (5 neighbors)
                    else:
                        #print('middle right edge')
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row + 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column - self._columns - 1])
                        cell.add_neighbor(self._currentGrid[row][column - self._columns - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column - self._columns - 1])
                # bottom row
                else:
                    #print('lower')
                    # 1. bottom left corner (3 neighbors)
                    if column == 0:
                        #print('lower left')
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row - 1][column + 1])
                        cell.add_neighbor(self._currentGrid[0][column])
                        cell.add_neighbor(self._currentGrid[0][column + 1])
                        cell.add_neighbor(self._currentGrid[row][self._columns - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][self._columns - 1])
                        cell.add_neighbor(self._currentGrid[0][column])
                    # 2. rest of the bottom row (5 neighbors)
                    elif column < (self._columns - 1):
                        #print('upper')
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row - 1][column + 1])
                        cell.add_neighbor(self._currentGrid[0][column - 1])
                        cell.add_neighbor(self._currentGrid[0][column + 1])
                        cell.add_neighbor(self._currentGrid[0][column])
                    # bottom right corner (3 neighbors)
                    else:
                        #print('upper right')
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[0][column - 1])
                        cell.add_neighbor(self._currentGrid[0][column])
                        cell.add_neighbor(self._currentGrid[row - 1][0])
                        cell.add_neighbor(self._currentGrid[row][0])