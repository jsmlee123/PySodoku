from re import S
import sys

from sodoku import Difficulty, Sodoku

def test_valid_row():
    board1 = Sodoku()
    custom_board = [["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]
    board1.load_board(custom_board)
    assert board1.verify_board() == True

    solve1 = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
    board1.load_board(solve1)
    assert board1._solve_board(solve1) == True
    board1.generate_board(Difficulty.MEDIUM)
    print(Sodoku.board_to_str(board1._board))
    print(Sodoku.board_to_str(board1._solution))
    #print(board1._solution)
    print("Verify Tests Passed")


def main():
    test_valid_row()

if __name__ == "__main__":
    main()