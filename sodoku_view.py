import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class SodokuView(QWidget):
    def __init__(self):
        
        super(SodokuView, self).__init__()
        self._curr_board = [['.' for x in range(9)] for y in range(9)]
        self._sol_board = None
        self._initUI()

    def _initUI(self):
        '''
        TODO:
            9x9 board in center of application, each should be text box to enter input
            Generate board button 
            Check board button
            Hint button
            Show solution button
            *Load custom board
        '''
        verify_placement = pyqtSignal()






def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()