import collections
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Model.sodoku import Difficulty

class SodokuView(QWidget):
    '''
    Init signals for inputs
    '''
    update = pyqtSignal()
    gen = pyqtSignal()
    reveal = pyqtSignal()
    check = pyqtSignal()
    help = pyqtSignal()
    

    def __init__(self) -> None:
        '''
        Init non-gui members of class
        '''
        super(SodokuView, self).__init__()
        self._curr_board = [['' for x in range(9)] for y in range(9)]
        self._cells = collections.defaultdict(QLineEdit)
        self.difficulty = Difficulty.EASY
        self._initUI()
        

    def _initUI(self) -> None:
        '''
        TODO:
            9x9 board in center of application, each should be text box to enter input - Done
            Generate board button - Done
            Check board button - Done
            Hint button - Done
            Show solution button - Done
            *Load custom board
        '''
        #Add background image
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('QWidget {background-image: url(View//sodoku.jpg);}')

        #verify_placement = pyqtSignal()
        self.resize(1000,800)
        self.setWindowTitle("PySodoku")

        title = QLabel("PySodoku", self)
        title.setFont(QFont('Times', 40))
        title.move(365,50)

        #combobox to choose difficulties
        self.combobox1 = QComboBox(self)
        self.combobox1.currentTextChanged.connect(self.change_difficulty)
        self.combobox1.resize(100,30)
        self.combobox1.move(100,540)
        self.combobox1.addItem('Easy')
        self.combobox1.addItem('Medium')
        self.combobox1.addItem('Hard')

        #board
        self.board = []
        self.init_sodoku()
        
        #Generate New Board
        self.generate = QPushButton('Generate New', self)
        self.generate.clicked.connect(self.gen)
        self.generate.move(100, 500)

        #Get Hint - Maybe Do Later
        self.hint = QPushButton('Show Hint', self)
        self.hint.clicked.connect(self.help)
        self.hint.move(100, 300)

        #Check Solution is correct
        self.verify = QPushButton('Check Solution', self)
        self.verify.clicked.connect(self.check)
        self.verify.move(825, 300)

        #Show Solution
        #Check Solution is correct
        self.solution = QPushButton('Reveal Solution', self)
        self.solution.clicked.connect(self.reveal)
        self.solution.move(825, 500)

        #Label which tells if solution is solved
        self.is_solved = QLabel('', self)
        self.is_solved.setAlignment(Qt.AlignCenter)
        self.is_solved.setFont(QFont('Arial', 30))
        self.is_solved.resize(500,100)
        self.is_solved.move(260, 650)

        #reveal widget
        self.show()
    
    def change_difficulty(self, diff : str):
        '''
        Change current set difficulty in view
        '''
        if diff == "Easy":
            self.difficulty = Difficulty.EASY
        elif diff == "Medium":
            self.difficulty = Difficulty.MEDIUM
        else:
            self.difficulty = Difficulty.HARD

    def set_curr_board(self, board : list[list[str]]) -> None:
        '''
        Change the current board to the given one
        '''
        self._curr_board = board

    def display(self):
        '''
        Sets the cells in the board to current one
        '''
        for i in range(9):
            for j in range(9):
                self._cells[(i,j)].setText(self._curr_board[i][j])

    def update_board(self) -> None:
        '''
        Updates the view board, if the input on the board was correct
        '''
        for i in range(9):
            for j in range(9):
                cell = self._cells[(i,j)]
                if cell.text() != self._curr_board[i][j]:
                    if cell.text() in ['1','2','3','4','5','6','7','8','9','']:
                        self._curr_board[i][j] = cell.text()
                    else:
                        cell.setText(self._curr_board[i][j])

    def init_sodoku(self) -> None:
        '''
        Init the sodoku board graphic cells 
        '''
        for i in range(9):
            for j in range(9):
                temp = QLineEdit(self)
                temp.setText(self._curr_board[i][j])
                temp.setAlignment(Qt.AlignCenter)
                temp.setFont(QFont('Arial', 20))
                temp.resize(50,50)
                temp.move(i * 50 + 285, j * 50 + 200)
                temp.textEdited.connect(lambda: self.update_board())
                temp.textEdited.connect(self.update)
                self._cells[(i,j)] = temp
