import tkinter as tk
from tkinter import messagebox

class KarmaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Karma's Calculator")
        
        
        self.root.attributes("-topmost", True)

        # window size
        self.root.geometry("500x400")
        
        # gui clolors
        self.bg_color = "#2E2E2E"
        self.fg_color = "#FFFFFF"
        self.button_color = "#444444"
        self.button_text_color = "#FFFFFF"
        
        # Configure the root window's background color
        self.root.configure(bg=self.bg_color)
        
        self.lives = 0
        self.blanks = 0

        self.create_widgets()

    def create_widgets(self):
        # Label for lives
        self.label_lives = tk.Label(self.root, text="Number of live rounds:", fg=self.fg_color, bg=self.bg_color, font=("Arial", 12))
        self.label_lives.grid(row=0, column=0, padx=20, pady=10, sticky="e")

        self.entry_lives = tk.Entry(self.root, width=20, font=("Arial", 12), bg="#444444", fg=self.fg_color, insertbackground="white")
        self.entry_lives.grid(row=0, column=1, padx=20, pady=10)

        # Label for blanks
        self.label_blanks = tk.Label(self.root, text="Number of blank rounds:", fg=self.fg_color, bg=self.bg_color, font=("Arial", 12))
        self.label_blanks.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        self.entry_blanks = tk.Entry(self.root, width=20, font=("Arial", 12), bg="#444444", fg=self.fg_color, insertbackground="white")
        self.entry_blanks.grid(row=1, column=1, padx=20, pady=10)

        # Button to set rounds
        self.button_set = tk.Button(self.root, text="Set Rounds", command=self.set_rounds, font=("Arial", 12), bg=self.button_color, fg=self.button_text_color)
        self.button_set.grid(row=2, column=0, columnspan=2, pady=20)

        # Label for showing current rounds and percentages
        self.label_status = tk.Label(self.root, text="Status:", fg=self.fg_color, bg=self.bg_color, font=("Arial", 12))
        self.label_status.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

        # Buttons for actions
        self.button_live = tk.Button(self.root, text="Shot Live Round (L)", command=self.shot_live, font=("Arial", 12), bg=self.button_color, fg=self.button_text_color)
        self.button_live.grid(row=4, column=0, padx=20, pady=10)

        self.button_blank = tk.Button(self.root, text="Shot Blank Round (B)", command=self.shot_blank, font=("Arial", 12), bg=self.button_color, fg=self.button_text_color)
        self.button_blank.grid(row=4, column=1, padx=20, pady=10)

        self.button_invert = tk.Button(self.root, text="Invert (I)", command=self.invert, font=("Arial", 12), bg=self.button_color, fg=self.button_text_color)
        self.button_invert.grid(row=5, column=0, padx=20, pady=10)

        self.button_restart = tk.Button(self.root, text="Restart (R)", command=self.restart, font=("Arial", 12), bg=self.button_color, fg=self.button_text_color)
        self.button_restart.grid(row=5, column=1, padx=20, pady=10)

    def set_rounds(self):
        try:
            self.lives = int(self.entry_lives.get())
            self.blanks = int(self.entry_blanks.get())

            if self.lives < 0 or self.blanks < 0:
                raise ValueError

            self.update_status()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter non-negative integers for rounds.")
    
    def update_status(self):
        total = self.lives + self.blanks
        live_percent = (self.lives / total) * 100 if total > 0 else 0
        blank_percent = (self.blanks / total) * 100 if total > 0 else 0

        status_text = f"Lives: {self.lives} ({live_percent:.2f}%)\nBlanks: {self.blanks} ({blank_percent:.2f}%)"
        self.label_status.config(text=status_text)

    def shot_live(self):
        if self.lives > 0:
            self.lives -= 1
            self.update_status()
        else:
            messagebox.showwarning("Warning", "No live rounds left!")

    def shot_blank(self):
        if self.blanks > 0:
            self.blanks -= 1
            self.update_status()
        else:
            messagebox.showwarning("Warning", "No blank rounds left!")

    def invert(self):
        if self.lives > 0 and self.blanks > 0:
            response = messagebox.askquestion("Invert", "Would you like to invert lives and blanks?")
            if response == "yes":
                self.lives, self.blanks = self.blanks, self.lives
                self.update_status()
                messagebox.showinfo("Inverted", "Lives and blanks have been inverted.")
        else:
            messagebox.showwarning("Warning", "Cannot invert, missing rounds in one of the categories.")

    def restart(self):
        self.lives = 0
        self.blanks = 0
        self.entry_lives.delete(0, tk.END)
        self.entry_blanks.delete(0, tk.END)
        self.update_status()
        messagebox.showinfo("Game Over", "Game over! Restarting...")

if __name__ == "__main__":
    root = tk.Tk()
    app = KarmaCalculator(root)
    root.mainloop()