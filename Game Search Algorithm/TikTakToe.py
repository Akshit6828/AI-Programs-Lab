# TikTakToe Game using Minimax with Alpha-Beta Pruning
import time  #For calculating Judgement time

class TikTakToe:
    def __init__(self):
        self.i = 0
        self.figure_grid_game()

    def start_game(self):
        while True:
            self.draw_board()
            self.result = self.is_end()

            # Printing the Winner at Game End
            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '.':
                    print("It's a tie!")

                self.figure_grid_game()
                return

            # 'X' player's turn
            if self.player_turn == 'X':

                while True:

                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print('Judgement Time : {} seconds'.format(round(end - start, 7)))
                    print('Suggested Move by Algorithm: [ {} , {} ] as [x , y ]'.format(qx, qy))

                    px = int(input('Enter X : '))
                    py = int(input('Enter Y : '))
                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            # Computer or AI's Turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'  
    

    def figure_grid_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player 'X' always plays first
        self.player_turn = 'X'

    def draw_board(self):
        if (self.i%2)==0:
            self.i += 1
            print('\n{} GRID PREVIEW AFTER COMPUTER MOVE {}'.format(7*'*' , 7*'*'))
        else:
            self.i += 1
            print('\n{} GRID PREVIEW AFTER YOUR MOVE {}'.format(7*'*' , 7*'*'))
            
        
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()
        
    # Validating Move
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True


    # Checking end of game and returning winner of game
    def is_end(self):
        # Straight Line(Vertical) Match Found
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Straight Line (Horizontal) Match Found
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # Main Diagnol(Preceding) Match Found
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second Diagnol(Non Preceding) Match Found
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # Check if Grid is Completely Filled
        for i in range(0, 3):
            for j in range(0, 3):
                # Continuing if Empty Space is found!
                if (self.current_state[i][j] == '.'):
                    return None

        # Returning '.' if tie is found
        return '.'

    # Player 'O'(Computer) is max
    def max(self):
        '''Possible values for maxv are:
        [-1 , 0 , 1] = [Loss, Tie, Win]
        '''
        # Setting Worst Value to = -2
        maxv = -2
        px = None
        py = None

        result = self.is_end()

        '''
        Validating game end and returning judgement time
        [-1 , 0 , 1] = [Loss , Tie , Win] respectively
        '''
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    # Updating maxv value
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting move to '.'
                    self.current_state[i][j] = '.'
        return (maxv, px, py)


    # Player 'X'(Human) is min
    def min(self):

        '''Possible values for maxv are:
        [-1 , 0 , 1] = [Loss, Tie, Win]
        '''

        # Setting Worst Value for minv
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

        return (minv, qx, qy)


if __name__ == "__main__":
    obj = TikTakToe()
    obj.start_game()                                       