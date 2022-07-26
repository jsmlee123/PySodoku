import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SodokuView(QWidget):
    def __init__(self):
        
        super(SodokuView, self).__init__()
        self._curr_board = [['.' for x in range(9)] for y in range(9)]
        self._static = []
        self._sol_board = None
        self._initUI()

    def _initUI(self):
        '''
        TODO:
            9x9 board in center of application, each should be text box to enter input - Done
            Generate board button 
            Check board button
            Hint button
            Show solution button
            *Load custom board
        '''
        #Add background image
        

        self.setAttribute(Qt.WA_StyledBackground, True)
        
        self.setStyleSheet('QWidget {background-image: url(sodoku.jpg);}')
        
        

        #verify_placement = pyqtSignal()
        self.resize(1000,800)
        self.setWindowTitle("PySodoku")

        title = QLabel("PySodoku", self)
        title.setFont(QFont('Times', 40))
        title.move(365,50)

        #board
        self.board = []
        self.init_sodoku()
        
        #Generate New Board
        generate = QPushButton('Generate New', self)
        generate.move(100, 500)

        #Get Hint - Maybe Do Later
        hint = QPushButton('Show Hint', self)
        hint.move(100, 300)

        #Check Solution is correct
        verify = QPushButton('Check Solution', self)
        verify.move(825, 300)

        #Show Solution
        #Check Solution is correct
        solution = QPushButton('Reveal Solution', self)
        solution.move(825, 500)

        


        self.show()
        #fwidget = QWidget()
        #fwidget.setGeometry(0,0,500,500)

    def set_curr_board(self, board):
        self._curr_board = board

    def init_sodoku(self):
        for i in range(9):
            for j in range(9):
                temp = QLineEdit(self)
                temp.setText(self._curr_board[i][j])
                temp.resize(50,50)
                temp.move(i * 50 + 285, j * 50 + 200)


def window():
   app = QApplication(sys.argv)
   view = SodokuView()
   app.exec()
   

if __name__ == '__main__':
   window()