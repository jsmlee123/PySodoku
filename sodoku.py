import sys
from typing import Union
from copy import deepcopy
import random
from enum import Enum


class Difficulty(Enum):
    '''
    Represents the different difficulties in sodoku and how many
    cells must be empty
    '''
    EASY = 45
    MEDIUM = 54
    HARD = 63

class Sodoku:
    '''
    Logic for sodoku
    '''
    def __init__(self) -> None:
        self._board = [['.' for x in range(9)] for y in range(9)]
        self._solution = None
        self.can_solve = False
    
    def load_board(self, board : list[list[str]]) -> None:
        '''
        Load in new custom board and its solution
        '''
        self._board = board
        self._solution = deepcopy(board)
        self.solve()


    def generate_board(self, difficulty = Difficulty.EASY) -> None:
        '''
        Generate board from scratch. Create random valid board 
        and remove numbers and store solution. Shuffling strategy taken
        from https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions
        '''

        board = [['.' for x in range(9)] for y in range(9)]
        self._solve_board(board) #solve this board to give us a basis

        for i in range(9):
            swap2 = random.randint(0,8)
            self._swap(board, i, swap2)
        self._shuffle_row(board)
        self._shuffle_col(board)
        self._shuffle_row_blocks(board)
        self._shuffle_col_blocks(board)

        self._solution = deepcopy(board)
        self._remove_random(board, difficulty.value)
        self._board = board
        

    def _remove_random(self, board : list[list[str]], remove_num : int) -> None:
        '''
        Removes the given number of cells from the board at random. This can be improved
        '''
        while remove_num:
            rand_x, rand_y = random.randint(0,8), random.randint(0,8)
            curr_val = board[rand_y][rand_x]
            if curr_val == '.':
                continue
            board[rand_y][rand_x] = '.'
            remove_num -= 1
    
    @staticmethod
    def board_to_str(board):
        '''
        Simple method to give any given board as a readable str
        '''
        res = ''
        for l in board:
            res += str(l) + '\n'
        return res

    
    def _swap(self, board : list[list[int]], i : int , j : int)-> None:
        '''
        Finds every instance of the numbers i and j on the board
        and swaps them for the other
        '''
        for y in range(9):
            for x in range(9):
                if board[x][y] == i: board[x][y] = j
                if board[x][y] == j: board[x][y] = i
    
    def _shuffle_row(self,board : list[list[int]]):
        '''
        Shuffle the rows in the given board at random
        '''
        for i in range(9):
            ranNum = random.randint(0,2)
            j = (i // 3) * 3 + ranNum
            board[i], board[j] = board[j], board[i]

    def _shuffle_col(self,board : list[list[int]]):
        '''
        Shuffle the columns in the given board at random
        '''
        for i in range(9):
            ranNum = random.randint(0,2)
            j = (i // 3) * 3 + ranNum
            for k in range(9):
                board[k][i], board[k][j] = board[k][j], board[k][i]
    
    def _shuffle_row_blocks(self,board : list[list[int]]):
        '''
        Shuffle the groups of 3 rows in the given board at random
        '''
        for i in range(3):
            j = random.randint(0,2)
            for k in range(3):
                board[i * 3 + k], board[j * 3 + k] = board[j * 3 + k], board[i * 3 + k]
    
    def _shuffle_col_blocks(self,board : list[list[int]]):
        '''
        Shuffle the groups of 3 columns in the given board at random
        '''
        for i in range(3):
            j = random.randint(0,2)
            for k in range(3):
                for z in range(9):
                    board[i * 3 + k][z], board[j * 3 + k][z] = board[j * 3 + k][z], board[i * 3 + k][z]

    def solve(self) -> None:
        '''
        Generate the solution board from the current board
        '''
        board = deepcopy(self._board)
        self.can_solve = self._solve_board(board)
        if self.can_solve: 
            self._solution = board

    def _solve_board(self, board) -> bool:
        '''
        Solve board. Return False if cannot solve, True if can solve
        '''
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for num in "123456789":
                        if self._verify_placement(board, i, j, num):
                            board[i][j] = num
                            if self._solve_board(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    

    def _verify_placement(self,board : list[list[int]], i : int, j : int, num : int):
        '''
        Verify that placement works. Using verify_board would be
        much more costly/ unneeded operations.
        '''
        for y in range(9):
            if board[y][j] == num:
                return False
            if board[i][y] == num:
                return False
            if board[3 * (i // 3) + y // 3][3 * (j // 3) + y % 3] == num:
                return False
        return True

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

    
