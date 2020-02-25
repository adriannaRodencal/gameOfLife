from cell import Cell
import toolbox
import random

class World(object):

    @classmethod
    def from_file(cls, filename):
        """
        Change the character that is displayed for cells.
        :param filename: path and filename to open text file.
        :return: new world made from text file
        """

        currentFile = open(filename, 'r')
        text = currentFile.readlines()

        textRow = text.split('\n')
        rows = len(textRow)
        columns = len(textRow[0])

        fileWorld = World(rows, columns)
        for rowNumber, row in enumerate(textRow):
            for columnNumber, cellText in enumerate(row):
                if cellText == Cell.displaySets['liveChar']['deadChar']:
                    fileWorld.set_cell(rowNumber, columnNumber, True)
        return fileWorld

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__grid = self.create_grid()
        self.create_neighbors()

    def __str__(self):
        string = ''
        for row in self.__grid:
            for cell in row:
                string += cell.__str__()
            string += '\n'
        return string

    def create_grid(self):
        """
        Create a grid using current world size and
        append to a list
        :param: none
        :return: grid
        """
        grid = []
        for rowNumber in range(self.__rows):
            row = []
            for columnNumber in range(self.__columns):
                row.append(Cell(rowNumber, columnNumber))
            grid.append(row)
        return grid

    def create_neighbors(self):
        """
        Using a loop create each cell's neighbors
        and a append it to a list
        :param: none
        :return: none
        """
        for row in self.__grid:
            for cell in row:
                #
                # There are some nine situations that we have to account for:
                #
                # 1. upper left corner (3 neighbors)
                # 2. rest of the top row (5 neighbors)
                # 3. upper right corner (3 neighbors)
                # 4. far left side (5 neighbors)
                # 5. normal cells (8 neighbors)
                # 6. far right side (5 neighbors)
                # 7. lower left corner (3 neighbors)
                # 8. rest of bottom row (5 neighbors)
                # 9. lower right corner (3 neighbors)
                #
                row = cell.get_row()
                column = cell.get_column()
                #print(f'({row},{column})')
                #print(self.__columns)
                # top row
                if row == 0:
                    # 1. upper left corner (3 neighbors)
                    if column == 0:
                        #print('upper left')
                        #TODO ! Talk to Mr. Sommerer about self.__columns
                        # being a list index out of range
                        cell.add_neighbor(self.__grid[row][self.__columns - 1])
                        cell.add_neighbor(self.__grid[row][column+1])
                        cell.add_neighbor(self.__grid[row+1][self.__columns - 1])
                        cell.add_neighbor(self.__grid[row+1][column])
                        cell.add_neighbor(self.__grid[row+1][column+1])
                        cell.add_neighbor(self.__grid[row][column+1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column+1])
                    # 2. rest of the top row (5 neighbors)
                    elif column < (self.__columns - 1):
                        #print('upper')
                        cell.add_neighbor(self.__grid[row][column-1])
                        cell.add_neighbor(self.__grid[row][column+1])
                        cell.add_neighbor(self.__grid[row+1][column-1])
                        cell.add_neighbor(self.__grid[row+1][column])
                        cell.add_neighbor(self.__grid[row+1][column+1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column-1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column+1])
                    # upper right corner (3 neighbors)
                    else:
                        #print('upper right')
                        cell.add_neighbor(self.__grid[row][column-1])
                        cell.add_neighbor(self.__grid[row+1][column-1])
                        cell.add_neighbor(self.__grid[row+1][column])
                        cell.add_neighbor(self.__grid[row][column-1])
                        cell.add_neighbor(self.__grid[row][column-self.__columns - 1])
                        cell.add_neighbor(self.__grid[row+1][column-self.__columns - 1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column-1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column])
                # middle row
                elif row < (self.__rows - 1):
                    #print('middle')
                    # 1. middle left edge (5 neighbors)
                    if column == 0:
                        #print('middle left edge')
                        cell.add_neighbor(self.__grid[row-1][column])
                        cell.add_neighbor(self.__grid[row-1][column+1])
                        cell.add_neighbor(self.__grid[row][column+1])
                        cell.add_neighbor(self.__grid[row+1][column])
                        cell.add_neighbor(self.__grid[row+1][column+1])
                        cell.add_neighbor(self.__grid[row-1][self.__columns - 1])
                        cell.add_neighbor(self.__grid[row][self.__columns - 1])
                        cell.add_neighbor(self.__grid[row+1][self.__columns - 1])
                    # 2. rest of the middle row (8 neighbors)
                    elif column < (self.__columns - 1):
                        #print('upper')
                        cell.add_neighbor(self.__grid[row-1][column - 1])
                        cell.add_neighbor(self.__grid[row-1][column])
                        cell.add_neighbor(self.__grid[row-1][column + 1])
                        cell.add_neighbor(self.__grid[row][column-1])
                        cell.add_neighbor(self.__grid[row][column+1])
                        cell.add_neighbor(self.__grid[row+1][column-1])
                        cell.add_neighbor(self.__grid[row+1][column])
                        cell.add_neighbor(self.__grid[row+1][column+1])
                    # 3. middle right edge (5 neighbors)
                    else:
                        #print('middle right edge')
                        cell.add_neighbor(self.__grid[row-1][column])
                        cell.add_neighbor(self.__grid[row-1][column-1])
                        cell.add_neighbor(self.__grid[row][column-1])
                        cell.add_neighbor(self.__grid[row+1][column])
                        cell.add_neighbor(self.__grid[row+1][column-1])
                        cell.add_neighbor(self.__grid[row-1][column-self.__columns - 1])
                        cell.add_neighbor(self.__grid[row][column-self.__columns - 1])
                        cell.add_neighbor(self.__grid[row+1][column-self.__columns - 1])
                # bottom row
                else:
                    #print('lower')
                    # 1. bottom left corner (3 neighbors)
                    if column == 0:
                        #print('lower left')
                        cell.add_neighbor(self.__grid[row][column+1])
                        cell.add_neighbor(self.__grid[row-1][column])
                        cell.add_neighbor(self.__grid[row-1][column+1])
                        cell.add_neighbor(self.__grid[0][column])
                        cell.add_neighbor(self.__grid[0][column-1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column])
                        cell.add_neighbor(self.__grid[row+1][column-self.__columns - 1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column-1])
                    # 2. rest of the bottom row (5 neighbors)
                    elif column < (self.__columns - 1):
                        #print('upper')
                        cell.add_neighbor(self.__grid[row][column-1])
                        cell.add_neighbor(self.__grid[row][column+1])
                        cell.add_neighbor(self.__grid[row-1][column-1])
                        cell.add_neighbor(self.__grid[row-1][column])
                        cell.add_neighbor(self.__grid[row-1][column+1])
                    # bottom right corner (3 neighbors)
                    else:
                        #print('upper right')
                        cell.add_neighbor(self.__grid[row][column-1])
                        cell.add_neighbor(self.__grid[row-1][column-1])
                        cell.add_neighbor(self.__grid[row-1][column])

    def set_cell(self, row, column, living):
        """
        Create a cell and set whether it is living
        or dead
        :param row: which row the cell is in
        :param column: which column the cell is in
        :param living: whether the state of living is
        True or False
        :return: none
        """
        self.__grid[row][column].set_living(living)

    def next_generation(self):
        """
        Run through a loop and change the state
        each cell is in then creat a new grid
        :param: none
        :return: none
        """
        newGrid = self.create_grid()
        for row in self.__grid:
            for cell in row:
                if cell.get_living() == True:
                    if cell.living_neighbors() in [2, 3]:
                        newGrid[cell.get_row()][cell.get_column()].set_living(True)
                else:
                    if cell.living_neighbors() == 3:
                        newGrid[cell.get_row()][cell.get_column()].set_living(True)

        self.__grid = newGrid
        self.create_neighbors()

    def randomize(self, percent):
        """
        Using the fill percent create a new world with
        random living and dead cells
        :param percent: percent of living cells
        :return: none
        """
        for row in self.__grid:
            for cell in row:
                if random.randrange(1, 100) <= percent:
                    cell.set_living(True)
                else:
                    cell.set_living(False)

    def percent_alive(self):
        """
        Read through the grid and create a percent
        telling how many cells are currenly alive
        :param: none
        :return: percentAlive
        """
        totalCells = 0
        percentAlive = 0
        living = 0
        for row in self.__grid:
            for cell in row:
                if cell.get_living() == True:
                    living += 1
        totalCells = self.__rows*self.__columns
        percentAlive = living/totalCells
        return toolbox.make_percent(percentAlive)

    def write_file(self, filename):
        """
        Open a new file and print out the current
        world and save it in worlds folder
        :param filename: name of file that world
        is saved under
        :return: none
        """
        with open(f'./worlds/filename', 'w+') as endFile:
            text = self.__str__()
            endFile.write(text)

    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns