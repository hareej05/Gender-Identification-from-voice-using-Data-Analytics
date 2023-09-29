import tkinter as tk
from tkinter import Button
from analyser import analyser_func


root = tk.Tk()
root.title("Gender Identification by Voice")
root.state('zoomed')


# Functions
def train_neural_net ():
    analyser_func('train', root, tk, output_text_area)


def analyse_voice ():
    analyser_func('analyse', root, tk, output_text_area)


# UI Components
project_name_label = tk.Label(root, text="Gender Identification by Voice", fg="black", font="Times 30 bold")
project_name_label.place(x=10, y=10, height=50)

train_net_button = Button(root, text='Train Neural Net', bg="gray", fg="white", font="Times 20 bold", width=25, height=2, command=train_neural_net)
train_net_button.place(x=10, y=80, width=300, height=50)

analyse_voice_button = Button(root, text='Analyse Voice', bg="gray", fg="white", font="Times 20 bold", width=25, height=2, command=analyse_voice)
analyse_voice_button.place(x=10, y=150, width=300, height=50)

output_text_area = tk.Text(padx=10, pady=10, font="Times 14")
output_text_area.pack(fill=tk.X, side=tk.BOTTOM)

root.geometry("500x300+100+100")  # Width x Height
root.mainloop()
