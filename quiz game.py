import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root, riddles):
        self.root = root
        self.root.title("Quiz")
        self.root.configure(bg="black")  # Set background color to black

        self.riddles = riddles
        self.current_riddle_index = 0
        self.score = 0

        self.display_start_page()

    def display_start_page(self):
        label_welcome = tk.Label(self.root, text="WELCOME TO THE QUIZ", font=("joker", 16, "bold"), fg="yellow", bg="black")
        label_welcome.pack(pady=20)

        continue_button = tk.Button(self.root, text="Start Quiz", command=self.display_riddle, font=("Helvetica", 12))
        continue_button.pack(pady=10)

    def display_riddle(self):
        self.clear_widgets()

        label_riddle = tk.Label(self.root, text=self.riddles[self.current_riddle_index]['riddle'], font=("Helvetica", 14), wraplength=400, justify="center", fg="yellow", bg="black")
        label_riddle.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set("1")  # default value

        for i, option in enumerate(self.riddles[self.current_riddle_index]['options']):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.radio_var, value=str(i + 1), font=("Helvetica", 12), fg="yellow", bg="black", selectcolor="red")
            radio_button.pack(pady=5)

        check_button = tk.Button(self.root, text="Check", command=self.check_answer, font=("Helvetica", 12))
        check_button.pack(pady=10)

    def check_answer(self):
        user_answer = int(self.radio_var.get())
        riddle = self.riddles[self.current_riddle_index]
        is_correct = user_answer == riddle['correct_option']

        self.show_result(is_correct, riddle['options'][riddle['correct_option'] - 1])

        next_button = tk.Button(self.root, text="Next", command=self.next_riddle, font=("Helvetica", 12))
        next_button.pack(pady=10)

    def show_result(self, is_correct, correct_answer):
        result_label = tk.Label(self.root, text="", font=("Helvetica", 12), fg="yellow", bg="black")
        result_label.pack(pady=5)

        if is_correct:
            result_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            result_label.config(text=f"Incorrect. The correct answer is: {correct_answer}", fg="red")

    def next_riddle(self):
        self.current_riddle_index += 1

        if self.current_riddle_index < len(self.riddles):
            self.display_riddle()
        else:
            self.show_final_score()

    def show_final_score(self):
        self.clear_widgets()

        final_score_label = tk.Label(self.root, text=f"Your final score is: {self.score}/{len(self.riddles)}", font=("Helvetica", 16, "bold"), fg="yellow", bg="black")
        final_score_label.pack(pady=20)

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def play(self):
        random.shuffle(self.riddles)
        self.display_riddle()

def main():
    riddles = [
        {
            'riddle': "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            'options': ["Wind", "Echo", "Cloud", "Radio"],
            'correct_option': 2
        },
        {
            'riddle': "What has keys but can't open locks?",
            'options': ["Keyboard", "Piano", "Lock", "Secret"],
            'correct_option': 2
        },
        {
            'riddle': "The more you take, the more you leave behind. What am I?",
            'options': ["Footsteps", "Memories", "Time", "Money"],
            'correct_option': 3
        }
    ]

    root = tk.Tk()
    root.configure(bg="black")  # Set overall background color to black
    quiz = QuizGame(root, riddles)
    root.mainloop()

if __name__ == "__main__":
    main()

