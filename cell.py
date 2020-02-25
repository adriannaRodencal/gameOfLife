
class Cell(object):

    displaySets = {'basic': {'liveChar': 'O', 'deadChar': '.'},
                    'stars': {'liveChar':'\u272D','deadChar':'\u2730'},
                    'weather': {'liveChar':'\u2600','deadChar':'\u2601'},
                    'spades': {'liveChar':'\u2660','deadChar':'\u2664'},
                    'atom': {'liveChar':'\u269B','deadChar':' '} }

    displaySet = 'basic'

    liveChar = displaySets[displaySet]['liveChar']
    deadChar = displaySets[displaySet]['deadChar']

    @classmethod
    def set_display(cls, displaySet):
        """
        Using classmethod set the current display set
        Using classmethod set the current display set
        and be able to change it
        :param displaySet: chosen set of characters that
        are printed during simulation
        :return: none
        """
        legalValues = cls.displaySets.keys()
        if displaySet in legalValues:
            cls.displaySet = displaySet
            cls.liveChar = cls.displaySets[displaySet]['liveChar']
            cls.deadChar = cls.displaySets[displaySet]['deadChar']
        elif displaySet == 'choice':
            cls.liveChar = input('What character would you like for your live cells? ')
            cls.deadChar = input('What character would you like for your dead cells? ')
        else:
            raise ValueError(f'DisplaySet must be in {legalValues}.')

    def __init__(self, row, column):
        self.__row = row
        self.__column = column
        self.living = False
        self.__neighbors = []

    def __str__(self):
        if self.living:
            return Cell.liveChar
        else:
            return Cell.deadChar

    def get_living(self):
        return self.living

    def set_living(self, state):
        if isinstance(state, bool):
            self.living = state
        else:
            raise TypeError('state must be boolean.')

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def add_neighbor(self, cell):
        """
        Add neighboring cell as a neighbor
        :param cell: row and column where the
        neighbor is located
        :return: none
        """
        #
        # Print statement below is for debugging. Comment
        # out you know all the neighbors are working.
        #
        #print(f'{self.__repr__()} add neighbor {cell.__repr__()}')
        self.__neighbors.append(cell)

    def living_neighbors(self):
        """
        Run through and count how many
        living neighbors the cell has.
        :param: none
        :return: neighborCount
        """
        neighborCount = 0
        for neighbor in self.__neighbors:
            if neighbor.get_living() == True:
                neighborCount += 1
        return neighborCount

    def __repr__(self):
        #
        # Here's a handy way to use if..else that we haven't talked about.
        #
        state = 'alive' if self.living else 'dead'
        return f'Cell({self.__row},{self.__column}) [{state}]'

    def debug(self):
        """
        Debug the neighbors in __init__
        :param: none
        :return: none
        """
        neighbors = len(self.__neighbors)
        string = self.__repr__() + f' neighbors: {self.living_neighbors()}/{neighbors}'
        for neighbor in self.__neighbors:
            string += '\n     ' + neighbor.__repr__()
        #print(string)