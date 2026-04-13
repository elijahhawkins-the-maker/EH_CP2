#EHCP2 where actual portfolio is made
import tkinter as tk

from fractal_gen.fg_main import main

import DND

from geo_calc.main import main as geo_calc_main

from word_counter.main_wc import main_menu as word_counter_main

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("EHCP2 Coding Portfolio")
        self.root.geometry("400x400")

        self.label = tk.Label(self.root, text="Welcome to EHCP2, by Elijah Hawkins")
        self.label.pack()

        self.button = tk.Button(self.root, text="Show Fractal Generator", command=main)
        self.button2 = tk.Button(self.root, text="Show DND", command=DND.main)
        self.button3 = tk.Button(self.root, text="Show Geo Calc", command=geo_calc_main)
        self.button4 = tk.Button(self.root, text="Show Word Counter", command=word_counter_main)

        self.button.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()

        self.root.mainloop()

class PortfolioGUI(GUI):
    def __init__(self):
        super().__init__()
        self.label.config(text="Welcome to the Portfolio")
        self.button.config(text="View Portfolio")
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

PortfolioGUI()