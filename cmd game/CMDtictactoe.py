class Board:
    def __init__(self):
        #   Create an list for the players to input their choice
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #   Print  the board, each element of the list and separate lines and columns
    def display(self, pos):
        print(f" {pos[0]} | {pos[1]} | {pos[2]}")
        print(" ---------")
        print(f" {pos[3]} | {pos[4]} | {pos[5]}")
        print(" ---------")
        print(f" {pos[6]} | {pos[7]} | {pos[8]}")

    #  Check for user's input,the range of the position and if the position is empty or taken
    def check_input(self, p, v, bo):
        p = p - 1
        if p < 0 or p > 8 or v < 1 or v > 2:
            return False
        if bo[p] == 'X' or bo[p] == "O":
            return False
            # Change the value from 1 and save it as 'X'
        else:
            if v == 1:
                bo[p] = "X"
            # Change the value from 2 and save it as 'O'
            elif v == 2:
                bo[p] = "O"
            return True



    # If there's one combination, end the game
    def winner(self):
        if self.board[0] == self.board[1] == self.board[2]:
            return True
        elif self.board[3] == self.board[4] == self.board[5]:
            return True
        elif self.board[6] == self.board[7] == self.board[8]:
            return True
        elif self.board[0] == self.board[3] == self.board[6]:
            return True
        elif self.board[1] == self.board[4] == self.board[7]:
            return True
        elif self.board[2] == self.board[5] == self.board[8]:
            return True
        elif self.board[0] == self.board[4] == self.board[8]:
            return True
        elif self.board[2] == self.board[4] == self.board[6]:
            return True
        else:
            return False

    # Check if the list's elements are 0 or filled
    def completed(self, bor):
        for i in range(len(bor), 0, -1):
            if i ==0:
                return True
            if bor[i-1] != "X" and bor[i-1] != "O":
                return False
        return True

x = Board()
while not x.winner() and not x.completed(x.board):
    x.display(x.board)
    position = int(input("Enter the number of the cell you would like to play: "))
    value = int(input("Input your choice(1 = X and 2 = O): "))
    if not x.check_input(position, value, x.board):
        print("Try again!")
x.display(x.board)
# TODO: When I change the value input to x and O, its takes it as wrong
