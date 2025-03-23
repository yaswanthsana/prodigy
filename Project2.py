import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        
        tk.Label(root, text="Guess a number between 1 and 100:").grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_guess = tk.Entry(root)
        self.entry_guess.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Button(root, text="Submit Guess", command=self.check_guess).grid(row=1, column=0, columnspan=2, pady=10)
    
    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1
            
            if guess < self.target_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif guess > self.target_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
    
    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry_guess.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
