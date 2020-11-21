from tkinter import *
from tkinter import messagebox
import sys
import os


class Game:
    def __init__(self):
        # Call tkinter
        self.root = Tk()
        # Assign a title to the window
        self.root.title("Tic Tac Toe 1.0")
        """  Please change the directory of the image you will save!"""
        self.root.iconbitmap("C:/Users/Noxyseras/Desktop/HomePython/ticto.ico")
        # X is first so is true
        self.clicked = True
        # times played
        self.count = 0
        self.p1 = StringVar()
        self.p2 = StringVar()
        """         adoifhdsuofhsdfhuoifshuofshdoufsdoufshdfhsdoifsdoifuifsdiuofsd"""
        self.player1 = Entry(self.root, textvariable=self.p1, bd=5)
        self.player1.grid(row=1, column=1, columnspan=8)
        self.player2 = Entry(self.root, textvariable=self.p2, bd=5)
        self.player2.grid(row=2, column=1, columnspan=8)

    # Disable buttons after the game ends
    def disableButton(self):
        bu1.configure(state=DISABLED)
        bu2.configure(state=DISABLED)
        bu3.configure(state=DISABLED)
        bu4.configure(state=DISABLED)
        bu5.configure(state=DISABLED)
        bu6.configure(state=DISABLED)
        bu7.configure(state=DISABLED)
        bu8.configure(state=DISABLED)
        bu9.configure(state=DISABLED)

    # If the button is clicked and the self.clicked is true or false, change the button text to either X or O
    def change(self, b):
        if b["text"] == " " and self.clicked == True:
            b["text"] = "X"
            self.clicked = False
            self.count += 1
            self.player2 = self.p2.get() + " Wins!"
            pa = self.p1.get() + " Wins!"
            self.winner()
            return self.player1
        elif b["text"] == " " and self.clicked == False:
            b["text"] = "O"
            self.clicked = True
            self.count += 1
            self.player1 = self.p2.get() + " Wins!"
            self.winner()
            return self.player2
        # If the user clicks the button that is already clicked and assigned a value, display a message
        else:
            messagebox.showwarning("Warning!",
                                   "The cell you are trying to click is already selected!\nTry another cell!")

    # If there's one combination, end the game and display the winner and call the function to disable the buttons
    def winner(self):
        # If there is a combination of X, end game and display the winner
        if (bu1['text'] == 'X' and bu2['text'] == 'X' and bu3['text'] == 'X' or
                bu4['text'] == 'X' and bu5['text'] == 'X' and bu6['text'] == 'X' or
                bu7['text'] == 'X' and bu8['text'] == 'X' and bu9['text'] == 'X' or
                bu1['text'] == 'X' and bu4['text'] == 'X' and bu7['text'] == 'X' or
                bu2['text'] == 'X' and bu5['text'] == 'X' and bu8['text'] == 'X' or
                bu3['text'] == 'X' and bu6['text'] == 'X' and bu9['text'] == 'X' or
                bu1['text'] == 'X' and bu5['text'] == 'X' and bu9['text'] == 'X' or
                bu3['text'] == 'X' and bu5['text'] == 'X' and bu7['text'] == 'X'):
            self.disableButton()
            messagebox.showinfo("Winner!", self.player1)

        # If there is a combination of X, end game and display the winner
        elif (bu1['text'] == 'O' and bu2['text'] == 'O' and bu3['text'] == 'O' or
              bu4['text'] == 'O' and bu5['text'] == 'O' and bu6['text'] == 'O' or
              bu7['text'] == 'O' and bu8['text'] == 'O' and bu9['text'] == 'O' or
              bu1['text'] == 'O' and bu4['text'] == 'O' and bu7['text'] == 'O' or
              bu2['text'] == 'O' and bu5['text'] == 'O' and bu8['text'] == 'O' or
              bu3['text'] == 'O' and bu6['text'] == 'O' and bu9['text'] == 'O' or
              bu1['text'] == 'O' and bu5['text'] == 'O' and bu9['text'] == 'O' or
              bu3['text'] == 'O' and bu5['text'] == 'O' and bu7['text'] == 'O'):
            self.disableButton()
            messagebox.showinfo("Winner!", self.player2)

        # if counter reached 9 times, and there is no winner yet, display the user that is a tie
        elif self.count == 9:
            self.disableButton()
            messagebox.showinfo("Tie..", "It's a tie!")

    # Function to restart the program
    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    x = Game()
    # Label to display the players their symbol
    label1 = Label(x.root, text="Player 1: X", font='Times 16 bold', bg='white', fg='black', height=1, width=8)
    label1.grid(row=0, column=0)
    label2 = Label(x.root, text="Player 2: O", font='Times 16 bold', bg='white', fg='black', height=1, width=8)
    label2.grid(row=1, column=0)
    """Restart the game"""
    again = Button(x.root, text="Retry", height=2, width=6, bg="red", command=x.restart_program)
    again.grid(row=2, column=0)

    bu1 = Button(x.root, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8,
                 command=lambda: x.change(bu1))
    bu1.grid(row=3, column=0)
    bu2 = Button(x.root, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8,
                 command=lambda: x.change(bu2))
    bu2.grid(row=3, column=1)
    bu3 = Button(x.root, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8,
                 command=lambda: x.change(bu3))
    bu3.grid(row=3, column=2)
    bu4 = Button(x.root, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8,
                 command=lambda: x.change(bu4))
    bu4.grid(row=4, column=0)
    bu5 = Button(x.root, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8,
                 command=lambda: x.change(bu5))
    bu5.grid(row=4, column=1)
    bu6 = Button(x.root, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8,
                 command=lambda: x.change(bu6))
    bu6.grid(row=4, column=2)
    bu7 = Button(x.root, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8,
                 command=lambda: x.change(bu7))
    bu7.grid(row=5, column=0)
    bu8 = Button(x.root, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8,
                 command=lambda: x.change(bu8))
    bu8.grid(row=5, column=1)
    bu9 = Button(x.root, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8,
                 command=lambda: x.change(bu9))
    bu9.grid(row=5, column=2)

    # Keep the window running
    x.root.mainloop()
