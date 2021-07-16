from player import Player

class Board:
    def __init__(self):
        self.rows=6
        self.columns=7
        self.clear()
    
    def clear(self):
        self.grid= [[None for j in range(self.columns)] for i in range(self.rows)]
    
    # To check whether a player has won
    def check_winning(self,player):
        id=player.get_id()

        # Check in Horizontal Direction
        for j in range(self.columns-3):
            for i in range(self.rows):
                if self.grid[i][j] == id and self.grid[i][j+1] == id and self.grid[i][j+2] == id and self.grid[i][j+3] == id:
                    return True
        
        # Check in Vertical Direction
        for j in range(self.columns):
            for i in range(self.rows-3):
                if self.grid[i][j] == id and self.grid[i+1][j] == id and self.grid[i+2][j] == id and self.grid[i+3][j] == id:
                    return True

        # Check Ascending Diagonal
        for j in range(self.columns-3):
            for i in range(self.rows-3):
                if self.grid[i][j] == id and self.grid[i+1][j+1] == id and self.grid[i+2][j+2] == id and self.grid[i+3][j+3] == id:
                    return True

        # Check Descending Diagonal
        for j in range(self.columns-3):
            for i in range(self.rows-3):
                if self.grid[i][j] == id and self.grid[i-1][j+1] == id and self.grid[i-2][j+2] == id and self.grid[i-3][j+3] == id:
                    return True
        
        return False
    
    # For each turn, player adds a new chip to a column of the board.
    # If the column is full return -1, else return the row to which the chip has been added

    def add_chip(self,player,column):
        for row in range(self.rows):
            cell=self.grid[row][column]
            if cell is None:
                self.grid[row][column]=player.get_id()
                return row
        return -1
