class World(object):

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__grid = self.create_grid()

    def __str__(self):
        """Return a string that represents the current generation. For example,
        a completely dead world (4x5) would look like this, assuming that
        Cell.deadChar is a period:
        .....
        .....
        .....
        .....
        A world (4x5) with one living cell would look like this, assuming
        that Cell.liveChar is an 'X' at position self.__grid[1][3]:
        .....
        ...X.
        .....
        .....
        Of course, you would not check on Cell.deadChar or Cell.liveChar. You
        would rely on the cell to know how it should be printed.
        """
        string = ''
        #
        # Your code goes here.
        #
        return string

    def create_grid(self):
        """Return the grid as a list of lists. There should be one list
        to contain the entire grid and in that list there should be one
        list to contain each row in the generation. Each of the "row lists"
        should contain one object of class Cell for each column in the world."""

        grid = [[]]
        while self.__rows in self.__columns:
            pass
        #
        # Your code goes here.
        #
        return grid

    def set_cell(self, row, column, living):
        """Change the state of the cell at self.__grid[row][column] to the
         value of living."""
        cell.set_living(living)

class Cell(object):

    liveChar = 'X'
    deadChar = '.'

    def __init__(self, row, column):
        """Given a row and a column, creates a cell that knows its row,
           column, living (all cells start off with living as False), and
           neighbors (all cells start off with an empty list for neighbors)."""
        self.__row = row
        self.__column = column
        self.__living = False
        self.__neighbors = []

    def __str__(self):
        """Returns either the liveChar or the deadChar for the Cell class
           depending on the state of the cell."""
        if self.__living == False:
            string = Cell.deadChar
        elif self.__living == True:
            string = Cell.liveChar
        return string

    def get_living(self):
        """Returns whether the cell is alive."""
        return self.__living

    def set_living(self, state):
        """Sets whether the cell is alive or dead."""
        self.__living = state

def test1():
    print('----Cell Tests----')
    c1 = Cell(1,3)
    print(c1)
    assert c1.get_living() == False
    assert c1.__str__() == Cell.deadChar
    c1.set_living(True)
    assert c1.get_living() == True
    assert c1.__str__() == Cell.liveChar
    assert c1._Cell__neighbors == []
    print('Finshed')

def test2():
    print('----World Tests----')

    w1 = World(3,4)
    print(w1)
    assert w1.__str__() == '....\n....\n....\n'
    w1.set_cell(0,0,True)
    w1.set_cell(0,3,True)
    w1.set_cell(2,0,True)
    w1.set_cell(2,3,True)
    print(w1)
    assert w1.__str__() == 'X..X\n....\nX..X\n'
    assert w1._World__rows == 3
    assert w1._World__columns == 4

if __name__ == '__main__':
    test1()
    test2()
