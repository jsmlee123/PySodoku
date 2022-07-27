import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Model.sodoku import Sodoku
from View.sodoku_view import SodokuView

class SodokuController:
    '''
    Controller to interact between sodoku view and model
    '''
    def __init__(self):
        self._app = QApplication(sys.argv)
        self._model = Sodoku()
        self._view = SodokuView()
        self.init()

    def init(self):
        self._view.update.connect(lambda : self.update_model())
        self._view.gen.connect(lambda : self.generate_model())
        self._view.reveal.connect(lambda : self.show_solution())
        self._view.check.connect(lambda : self.verify_solution())
        self._view.help.connect(lambda : self.get_hint())

    def get_hint(self):
        self._model.get_hint()
        self.update_view()
        self._view.display()
    
    def verify_solution(self):
        '''
        '''
        if self._model.is_solved():
            self._view.is_solved.setText("Solved")
        else:
            self._view.is_solved.setText("Unsolved")

    def show_solution(self):
        '''
        '''
        self._model.set_solved()
        self.update_view()
        self._view.display()
    
    def generate_model(self):
        '''
        '''
        self._model.generate_board(self._view.difficulty)
        self.update_view()
        self._view.display()
        self._view.is_solved.setText("")

    def update_view(self):
        for i in range(9):
            for j in range(9):
                model_cell = self._model._board[i][j]
                view_cell = self._view._curr_board[i][j]
                if model_cell != view_cell:
                    self._view._curr_board[i][j] = model_cell
        

    def update_model(self):
        for i in range(9):
            for j in range(9):
                model_cell = self._model._board[i][j]
                view_cell = self._view._curr_board[i][j]
                if model_cell != view_cell:
                    if self._model.set_val(i,j,view_cell) :
                        return
                    else:
                        self.update_view()
                        self._view.display()
    def run(self):
        self._view.show()
        return self._app.exec_()


    