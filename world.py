from cell import Cell
from rules import Rules
import toolbox
import random

class World(object):

    @classmethod
    def from_file(cls, filename, worldType):
        """
        Given a properly formatted text file, return a new World object.
        :param filename: path and filename to the text file.
        :return: a new World object made from the text file.
        """
        with open(filename, 'r') as myFile:
            text = myFile.readlines()

        rows = len(text)
        columns = len(text[0])


        newWorld = worldType(rows, columns, worldType)
        for rowNumber, row in enumerate(text):
            for columnNumber, cellText in enumerate(row):
                if cellText == Cell.liveChar:
                    newWorld.set_cell(rowNumber, columnNumber, True)
        return newWorld


    def __init__(self, rows, columns, worldType,  percent = 50):
        self._rows = rows
        self._columns = columns
        self.__percent = percent
        self.__worldType = worldType
        self._currentGrid = self.create_grid()
        self.__age1Grid = None
        self.__age2Grid = None
        self.__age3Grid = None
        self.create_neighbors()

    def __str__(self):
        string = ''
        for row in self._currentGrid:
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
        for rowNumber in range(self._rows):
            row = []
            for columnNumber in range(self._columns):
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
        for row in self._currentGrid:
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
                # print(f'({row},{column})')
                # top row
                if row == 0:
                    # 1. upper left corner (3 neighbors)
                    if column == 0:
                        # print('upper left')
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row + 1][column + 1])
                    # 2. rest of the top row (5 neighbors)
                    elif column < (self._columns - 1):
                        # print('upper row')
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row + 1][column + 1])
                    # 3. upper right corner (3 neighbors)
                    else:
                        # print('upper right')
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                # middle row
                elif row < (self._rows - 1):
                    # 4. far left side (5 neighbors)
                    if column == 0:
                        # print('left side')
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row - 1][column + 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row + 1][column + 1])
                    # 5. normal cells (8 neighbors)
                    elif column < (self._columns - 1):
                        # print('middle')
                        cell.add_neighbor(self._currentGrid[row - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row - 1][column + 1])
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                        cell.add_neighbor(self._currentGrid[row + 1][column + 1])
                    # 6. far right side (5 neighbors)
                    else:
                        # print('right side')
                        cell.add_neighbor(self._currentGrid[row - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row + 1][column])
                # bottom row
                else:
                    # 7. lower left corner (3 neighbors)
                    if column == 0:
                        # print('lower left')
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row - 1][column + 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                    # 8. rest of the bottom row (5 neighbors)
                    elif column < (self._columns - 1):
                        # print('lower row')
                        cell.add_neighbor(self._currentGrid[row - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row - 1][column + 1])
                        cell.add_neighbor(self._currentGrid[row][column - 1])
                        cell.add_neighbor(self._currentGrid[row][column + 1])
                    # 9. lower right corner (3 neighbors)
                    else:
                        # print('lower right')
                        cell.add_neighbor(self._currentGrid[row - 1][column - 1])
                        cell.add_neighbor(self._currentGrid[row - 1][column])
                        cell.add_neighbor(self._currentGrid[row][column - 1])

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
        self._currentGrid[row][column].set_living(living)

    def next_generation(self):
        """
        Run through a loop and change the state
        each cell is in then creat a new grid
        :param: none
        :return: none
        """
        #TODO! Percent will not work all of a sudden
        newGrid = self.create_grid()
        print(Rules.surviveNum)
        print(Rules.bornNum)
        for row in self._currentGrid:
            for cell in row:
                if cell.get_living() == True:
                    if str(cell.living_neighbors()) in str(Rules.surviveNum):
                        newGrid[cell.get_row()][cell.get_column()].set_living(True)
                else:
                    if str(cell.living_neighbors()) in str(Rules.bornNum):
                        newGrid[cell.get_row()][cell.get_column()].set_living(True)

        self.__age3Grid = self.__age2Grid
        self.__age2Grid = self.__age1Grid
        self.__age1Grid = self._currentGrid
        self._currentGrid = newGrid
        self.create_neighbors()

    def randomize(self, percent):
        """
        Using the fill percent create a new world with
        random living and dead cells
        :param percent: percent of living cells
        :return: none
        """
        for row in self._currentGrid:
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
        for row in self._currentGrid:
            for cell in row:
                if cell.get_living() == True:
                    living += 1
        totalCells = self._rows * self._columns
        percentAlive = living/totalCells
        return toolbox.make_percent(percentAlive)

    def save(self, filename):
        """
        Save the world as a text file.
        :param filename: path and filename with '.life' at the end.
        :return: None
        """
        currentDisplaySet = Cell.displaySet
        Cell.set_display('basic')
        text = self.__str__()
        Cell.set_display(currentDisplaySet)
        with open(filename, 'w') as myFile:
            myFile.write(text)

    def rerun(self):
        """
        Check to see if current generation is repeated or not
        :param: none
        :return: boolean
        """
        if str(self._currentGrid) in [str(self.__age1Grid), str(self.__age2Grid), str(self.__age3Grid)]:
            return False

        else:
            return True

    def get_rows(self):
        return self._rows

    def get_columns(self):
        return self._columns