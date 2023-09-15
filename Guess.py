import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Guess the number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1

        if guess < self.target_number:
            self.result_label.config(text=f"Try higher. Attempts: {self.attempts}")
        elif guess > self.target_number:
            self.result_label.config(text=f"Try lower. Attempts: {self.attempts}")
        else:
            self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
