import tkinter as tk
from tkinter import messagebox
import random

# Word list for the game
WORDS = ["python", "hangman", "coding", "interface", "programming", "data", "science"]

class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x400")
        
        # Game variables
        self.word = random.choice(WORDS)
        self.guessed_word = ["_" for _ in self.word]
        self.remaining_attempts = 6
        self.guessed_letters = set()
        
        # UI Elements
        self.create_widgets()
        self.update_display()
    
    def create_widgets(self):
        # Word display
        self.word_label = tk.Label(self.root, text="", font=("Arial", 20))
        self.word_label.pack(pady=20)
        
        # Input field for guesses
        self.entry = tk.Entry(self.root, font=("Arial", 16), width=5, justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.handle_guess)
        
        # Guess button
        self.guess_button = tk.Button(self.root, text="Guess", font=("Arial", 14), command=self.handle_guess)
        self.guess_button.pack(pady=5)
        
        # Remaining attempts
        self.attempts_label = tk.Label(self.root, text=f"Remaining Attempts: {self.remaining_attempts}", font=("Arial", 14))
        self.attempts_label.pack(pady=10)
        
        # Incorrect guesses
        self.incorrect_label = tk.Label(self.root, text="Incorrect Guesses: None", font=("Arial", 12))
        self.incorrect_label.pack(pady=10)
    
    def update_display(self):
        # Update guessed word
        self.word_label.config(text=" ".join(self.guessed_word))
        # Update remaining attempts
        self.attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")
        # Update incorrect guesses
        incorrect_guesses = ", ".join(self.guessed_letters)
        self.incorrect_label.config(text=f"Incorrect Guesses: {incorrect_guesses or 'None'}")
    
    def handle_guess(self, event=None):
        guess = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)
        
        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single valid letter.")
            return
        
        if guess in self.guessed_letters or guess in self.guessed_word:
            messagebox.showinfo("Already Guessed", f"You've already guessed '{guess}'.")
            return
        
        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess
        else:
            self.remaining_attempts -= 1
            self.guessed_letters.add(guess)
        
        self.update_display()
        self.check_game_status()
    
    def check_game_status(self):
        if "_" not in self.guessed_word:
            messagebox.showinfo("Congratulations!", "You guessed the word! You win!")
            self.reset_game()
        elif self.remaining_attempts <= 0:
            messagebox.showinfo("Game Over", f"You ran out of attempts! The word was '{self.word}'.")
            self.reset_game()
    
    def reset_game(self):
        self.word = random.choice(WORDS)
        self.guessed_word = ["_" for _ in self.word]
        self.remaining_attempts = 6
        self.guessed_letters = set()
        self.update_display()

# Create the app window
root = tk.Tk()
app = HangmanApp(root)
root.mainloop()
