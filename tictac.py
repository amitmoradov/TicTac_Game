import tkinter as tk  # מייבא את ספריית Tkinter
from tkinter import messagebox  # מייבא מודול להצגת חלונות הודעות ב-Tkinter

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()  # יצירת חלון חדש ב-Tkinter
        self.window.title("Tic Tac Toe")  # נתינת כותרת לחלון

        self.players = ["X", "O"]  # מערך של השחקנים
        self.current_player_index = 0  # השחקן הנוכחי באינדקס 0
        self.num_wins = [0, 0]  # מספר הניצחונות לכל שחקן

        self.board = [["" for _ in range(3)] for _ in range(3)]  # לוח המשחק בגודל 3x3

        self.setup_gui()  # הגדרת ממשק המשתמש

    def setup_gui(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]  # מערך הלחצנים בחלון

        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.window, text="", width=10, height=4, command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn  # הוספת הלחצן למערך הלחצנים

        self.label = tk.Label(self.window, text=f"Player {self.players[self.current_player_index]}'s turn", font=("Arial", 14))
        self.label.grid(row=3, columnspan=3)  # הגדרת תווית עם התור של השחקן הנוכחי

        self.stats_label = tk.Label(self.window, text=f"Wins - Player X: {self.num_wins[0]}, Player O: {self.num_wins[1]}", font=("Arial", 12))
        self.stats_label.grid(row=4, columnspan=3)  # הגדרת תווית עם נתוני סטטיסטיקות

    def on_click(self, row, col):
        if self.board[row][col] == "":  # בדיקה האם הלחצן לא נלחץ עד כה
            self.board[row][col] = self.players[self.current_player_index]  # הוספת סימן השחקן הנוכחי ללוח המשחק
            self.update_button(row, col)  # עדכון הלחצן בממשק המשתמש

            if self.check_winner(row, col):  # בדיקה האם יש ניצחון
                self.num_wins[self.current_player_index] += 1  # עדכון מספר הניצחונות
                self.update_stats_label()  # עדכון תווית סטטיסטיקות
                if messagebox.askyesno("Game Over", f"Player {self.players[self.current_player_index]} wins!\nDo you want to play again?"):
                    self.reset_game()  # איפוס המשחק אם השחקן רוצה לשחק שוב
                else:
                    self.window.destroy()  # סגירת החלון אם השחקן לא רוצה לשחק שוב
            elif self.check_draw():  # בדיקה האם יש תיקו
                if messagebox.askyesno("Game Over", "It's a draw!\nDo you want to play again?"):
                    self.reset_game()  # א
                    self.reset_game()  # איפוס המשחק אם השחקן רוצה לשחק שוב
                else:
                    self.window.destroy()  # סגירת החלון אם השחקן לא רוצה לשחק שוב
            else:
                self.switch_player()  # מעבר לשחקן הבא

    def update_button(self, row, col):
        button = self.buttons[row][col]
        button.config(text=self.players[self.current_player_index], state="disabled")  # עדכון הלחצן

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
        self.label.config(text=f"Player {self.players[self.current_player_index]}'s turn")  # החלפת השחקן הנוכחי בלייבל

    def check_winner(self, row, col):
        # בדיקה אם יש ניצחון לפי שורה
        if all(self.board[row][i] == self.players[self.current_player_index] for i in range(3)):
            return True

        # בדיקה אם יש ניצחון לפי עמודה
        if all(self.board[i][col] == self.players[self.current_player_index] for i in range(3)):
            return True

        # בדיקה אם יש ניצחון לפי אלכסונים
        if all(self.board[i][i] == self.players[self.current_player_index] for i in range(3)) or \
           all(self.board[i][2-i] == self.players[self.current_player_index] for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))  # בדיקה האם יש תיקו

    def update_stats_label(self):
        self.stats_label.config(text=f"Wins - Player X: {self.num_wins[0]}, Player O: {self.num_wins[1]}")  # עדכון לייבל סטטיסטיקות

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                button = self.buttons[i][j]
                button.config(text="", state="normal")  # איפוס הלחצנים
                self.board[i][j] = ""  # איפוס הלוח

        self.current_player_index = 0  # השחקן הנוכחי
        self.label.config(text=f"Player {self.players[self.current_player_index]}'s turn")  # עדכון לייבל תור השחקן

    def run(self):
        self.window.mainloop()  # הפעלת הממשק הגרפי

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
