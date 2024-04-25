arr2d = [[2] * 4 for j in range(4)]  # The right way

class TicTacToe:
    
    def __init__(self):
        self.__board = [[' '] * 3 for j in range(3)]
        self.__player = 'X'
        

    def mark(self, i, j):
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self.__board[i][j] != '':
            raise ValueError('Board position occupied')
        if self.winner( ) is not None:
            raise ValueError('Game is already complete')
        self.__board[i][j] = self.__player
        if self.__player == 'X' :
            self.__player = 'O'
        else:
            self.__player = 'X'
            
    
    def is_win(self, mark):
        board = self.__board # local variable for shorthand
        return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
        mark == board[1][0] == board[1][1] == board[1][2] or # row 1
        mark == board[2][0] == board[2][1] == board[2][2] or # row 2
        mark == board[0][0] == board[1][0] == board[2][0] or # column 0
        mark == board[0][1] == board[1][1] == board[2][1] or # column 1
        mark == board[0][2] == board[1][2] == board[2][2] or # column 2
        mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
        mark == board[0][2] == board[1][1] == board[2][0]) # rev diag
        

    def winner(self):
        for mark in 'XO' :
            if self.is_win(mark):
                return mark
        return None
    
   
    def __str__(self):
        rows = [ '|'.join(self.__board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)
    

if __name__ == '__main__':
    game = TicTacToe()
    # X moves: # O moves:
    game.mark(1, 1); game.mark(0, 2)
    game.mark(2, 2); game.mark(0, 0)
    game.mark(0, 1); game.mark(2, 1)
    game.mark(1, 2); game.mark(1, 0)
    game.mark(2, 0)     
    print(game)
    winner = game.winner( )
    if winner is None:
        print('Tie')
    else:
        print(winner, 'wins' )
 
    
        

