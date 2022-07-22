import sys
from typing import Union
from copy import copy, deepcopy

class sodoku:
    '''
    Logic for sodoku
    '''
    def __init__(self):
        self._board = [['.' for x in range(9)] for y in range(9)]
        self._solution = None
    
    def load_board(self, board : list[list[str]]):
        '''
        Load in new board and its solution
        '''
        self._board = board
        self._solution = self.solve_board()


    def generate_board(self):
        '''
        Generate board from scratch
        '''
    def solve_board(self):
        '''
        Solve board 
        '''

    def verify_board(self) -> bool:
        '''
        Verify Board is correct
        '''
        return self._valid_groups() and self._valid_row() and self._valid_column()
    def get_board(self) -> list[list[str]]:
        '''
        Return copy of board
        '''
        return deepcopy(self._board)

    def get_solution(self) -> list[list[str]]:
        '''
        Return copy of solution
        '''
        return deepcopy(self._solution)

    def set_val(self, x : int, y : int, val : str):
        '''
        Set cell in board
        '''
        self._board[x][y] = val

    def delete_val(self,x,y):
        '''
        Delete cell in board
        '''
        self._board[x][y] = '.'

    def _valid(self,group : Union[list,tuple]) -> bool:
        '''
        Verify unique numbers in group
        '''
        unit = [cell for cell in group if cell != '.']
        return len(set(unit)) == len(unit)

    def _valid_row(self) -> bool:
        '''
        Return if given row is valid
        '''
        for row in self._board:
            if not self._valid(row):
                return False
        return True

    def _valid_column(self) -> bool:
        '''
        Return if given column is valid
        '''
        for column in zip(*self._board):
            if not self._valid(column):
                return False
        return True

    def _valid_groups(self) -> bool:
        '''
        Return if all 3x3 groups are valid
        '''
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                group = [self._board[m][n] for m in range(i, i + 3) for n in range(j, j + 3)]
                if not self._valid(group):
                    return False
        return True

    
        