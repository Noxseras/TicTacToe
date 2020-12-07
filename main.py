from tkinter import *
from tkinter import messagebox


# class for the tkinter window
class Window:
    def __init__(self):
        # Call tkinter
        self.r = Tk()
        # Assign a title to the window
        self.r.title("Tic Tac Toe 1.1")


class PLayer:
    def __init__(self):
        # call the Window class
        self.roott = Window().r
        # Assign both names as StringVar() in order to change it later
        self.player1 = StringVar()
        self.player2 = StringVar()
        # Let the user to enter the username for the game
        self.player1 = Entry(self.roott, textvariable=self.player1, bd=5)
        self.player1.grid(row=1, column=1, columnspan=8)
        self.player2 = Entry(self.roott, textvariable=self.player2, bd=5)
        self.player2.grid(row=2, column=1, columnspan=8)
        # set both scores to 0
        self.score1 = 0
        self.score2 = 0


class Board:
    def __init__(self):
        # assign a grid for the game
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # call the Window class again
        self.root = Window().r
        self.current = "X"
        self.label_1 = Label(text=f"It's {self.current} turn", font=('normal', 22, 'bold'))
        self.label_1.grid(row=3, column=1)

    # Check the cells of the game
    def check_cells(self):
        for i in range(3):
            for j in range(3):
                # Check if the list's row and column are empty, allow the players to play
                if self.grid[i][j]['text'] == "-":
                    return True
        return False  # if the for loop ends return false and end the game

    def winner(self):
        # if there is any combination in the same row, return 1 for the game function
        for i in range(3):
            if self.grid[i][0]['text'] == self.grid[i][1]['text'] == self.grid[i][2]['text'] != "-":
                return 1
            # if there is any combination in the same column as well, return 1 for the game function
        for j in range(3):
            if self.grid[0][j]['text'] == self.grid[1][j]['text'] == self.grid[2][j]['text'] != "-":
                return 1
            # Or if there is any diagonally, return 1
        if self.grid[0][0]['text'] == self.grid[1][1]['text'] == self.grid[2][2]['text'] != "-":
            return 1
        elif self.grid[0][2]['text'] == self.grid[1][1]['text'] == self.grid[2][0]['text'] != "-":
            return 1
        # if there is not any combinations, return -1 which means it is a tie
        elif not self.check_cells():
            return -1
        # Else return 0 , and change player who's playing
        else:
            return 0

    # Assign and change players. PLus check display if someone won or its a tie
    def game(self, r, c):
        # if the self.winner() returns 1
        if self.grid[r][c]['text'] == "-" and self.winner() == 0:
            # if the player who starts is X
            if self.current == "X":
                # when the button is pressed, change the text of the cell to X
                self.grid[r][c].config(text='X')
                # If no one won, change the player
                if self.winner() == 0:
                    self.current = "O"
                    self.label_1.config(text="It's O's turn")
                # if the player "X" is the winner display message
                elif self.winner() == 1:
                    self.label_1.config(text="X win!")
                    return False
                # If the self.winner function returns -1, display the players "Draw"
                elif self.winner() == -1:
                    self.label_1.config(text="Tie!")
            # Now for Player 0(same code as for the player X)
            elif self.current == "O":
                # when the button is pressed, change the text of the cell to O
                self.grid[r][c].config(text='O')
                # If no one won, change the player
                if self.winner() == 0:
                    self.current = "O"
                    self.label_1.config(text="It's X's turn")
                # if the player "O" is the winner display message
                elif self.winner() == 1:
                    self.label_1.config(text="O win!")
                    return False
                # If the self.winner function returns -1, display the players "Draw"
                elif self.winner() == -1:
                    self.label_1.config(text="Tie!")
                    return False


x = Board()
for i in range(3):
    for j in range(3):
        # assign the board cells as buttons, for each cell there will be it's own button
        x.grid[i][j] = Button(x.root, text="-", font='Times 20 bold', bg='gray', fg='black', height=4,
                              # the r and c are asigned from the board[i][j]
                              width=8, command=lambda r=i, c=j: x.game(r, c))
        x.grid[i][j].grid(row=i, column=j)
x.root.mainloop()
