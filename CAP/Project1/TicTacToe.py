# Code for CAP 4630
# Author: Hunter Bresler (Based on Kylie Ying's code provided in the guidelines pdf)
# Group: Hunter Bresler and Chris Chung

import math

class TicTacToe:    
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None
        self.turn = 'X'
        self.count = 0

    def print_board(self):
        # shows each square's corresponding number on the board
        for count, x in enumerate(self.board):
            print(f"| {x} ", end = "")
            if (count + 1) % 3 == 0: print(f"|")
        print()

    @staticmethod
    def print_board_example():
        for i in range(9):
            print(f"| {i + 1} ", end = "")
            if (i + 1) % 3 == 0: print(f"|")
        print()

    def get_players(self):
        # gets input on whether X and or O are human or computer players
        self.x_player = input("The player with X is ('c' for computer, 'h' for human): ")
        self.o_player = input("The player with O is ('c' for computer, 'h' for human): ")

        # check inputs 
        if self.x_player != 'c' and self.x_player != 'h':
            print("Invalid inputs, try again.")
            self.get_players()
        if self.o_player != 'c' and self.o_player != 'h':
            print("Invalid inputs, try again.")
            self.get_players()

    def get_move_human(self):
        # gets input for what move to play
        try:
            result = int(input(f"Enter where you would like to put an {self.turn} (#1-9): ")) - 1
        except:
            print("Invalid input, try again")
            result = self.get_move_human()

        return result

    def get_move_AI(self):
        print("The computer moved.")
        return self.minimax(self.turn, self.turn)['position']

    
    def minimax(self, current_player, ai_player, alpha=-math.inf, beta=math.inf):
        # minimax algorithm with alpha-beta pruning
        ai_player = ai_player
        if current_player == 'X':
            other_player = 'O'
        else:
            other_player = 'X'

        # base cases 
        if self.winner == other_player and other_player == ai_player:   # win
            return {'position': None, 'score': 1 * (self.empty_squares() + 1)}
        
        elif self.winner == other_player: # lose
            return {'position': None, 'score': -1 * (self.empty_squares() + 1)} 
        
        elif self.empty_squares() == 0 and self.winner == None: # tie
            return {'position': None, 'score': 0}

        # set the default value for the best move
        if current_player == ai_player:
            best_score = {'position': None, 'score': -math.inf}
        else:
            best_score = {'position': None, 'score': math.inf}

        for move in self.legal_moves():
            # 1. try a move
            self.play_move(move, current_player)

            # 2. recurse to generate the best outcome from that move
            # simulates all possible games after said move
            temp_score = self.minimax(other_player, ai_player, alpha, beta)


            # 3. undo the move
            self.board[move] = ' '
            self.winner = None
            temp_score['position'] = move
            
            # 4. if the move's score was better than best_score, update best_score
            if current_player == ai_player:
                if temp_score['score'] > best_score['score']:
                    best_score = temp_score

                # alpha-beta pruning
                alpha = max(alpha, best_score['score'])
                if beta <= alpha:
                    break
            else:
                if temp_score['score'] < best_score['score']:
                    best_score = temp_score

                # alpha-beta pruning
                beta = min(beta, best_score['score'])
                if beta <= alpha:
                    break

        #count an extra game   
        self.count += 1
        return best_score


    def empty_squares(self):
        return self.board.count(' ')
    
    def legal_moves(self):
        # returns a list of legal moves
        return [(i) for i, square in enumerate(self.board) if square == ' ']

    def play_move(self, square, letter):
        # Makes a move if it's legal, else return false
        if square in self.legal_moves(): 
            self.board[square] = letter

            # check if it is a winning move
            if self.is_winner(square, letter):
                self.winner = letter

            return True
        else:
            return False
        
    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def is_winner(self, square, letter):
        #Kylie Ying's code, the code is simple and I don't know how to do the indexing myself
        #Not claiming them as my own
        # check if the last move was a winning move
        #check row
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([sq == letter for sq in row]):
            return True
        
        #check col
        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all([sq == letter for sq in col]):
            return True
        
        #check diagonals
        diagonal1 = [self.board[i] for i in [0, 4, 8]]
        if all([sq == letter for sq in diagonal1]):
            return True
        diagonal2 = [self.board[i] for i in [2, 4, 6]]
        if all([sq == letter for sq in diagonal2]):
            return True
        
        # If no winner is found, return false
        return False
    
    def play(self, player):
        # plays
        if player == 'c':
            square = self.get_move_AI()
        if player == 'h':
            square = self.get_move_human()
        flag = self.play_move(square, self.turn)
        
        # make sure inputs are valid
        if flag == False: 
            print("Invalid input, try again")
            self.play(player)
        else:
            self.print_board()
            self.change_turn()


    def game(self):
        # get players
        self.get_players()
        self.print_board_example()

        # play game
        while self.empty_squares() > 0:
            if self.winner == 'X' or self.winner == 'O': 
                print(f"{self.winner} Wins!")
                #print(f"There were {self.count} branches observed")
                break
            if self.turn == 'X': 
                self.play(self.x_player)
            elif self.turn == 'O': 
                self.play(self.o_player)

        # if there are no legal moves, and nobody has won, the game is a draw
        if self.winner == None: 
            print("The game ended in a tie.")
            #print(f"There were {self.count} branches observed")

obj = TicTacToe()
obj.game()