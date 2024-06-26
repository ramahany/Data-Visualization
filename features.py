import tkinter as tk
import ttkbootstrap as ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class NormalizeFeatures:

    def __init__(self, win: ttk.Toplevel, x: np.array, y: np.array):
        self.win = win
        self.win.title('Normalize feature')
        self.win.geometry('600x600')

        self.feature = x
        self.label = y

        self.norm_menu = ttk.Menubutton(self.win, bootstyle='info', text='original data')
        self.norm_menu.place(relx=0.05, rely=0.05, relwidth=0.4)

        # add a menu to it
        self.normalization_options = ['original data', 'scaling to a range(mean)', 'clipping', 'log scaling', 'z-score']

        inside_menu = ttk.Menu(self.norm_menu)
        for j in self.normalization_options:
            inside_menu.add_radiobutton(label=j, command=lambda j=j: self.change_plot(j))
        self.norm_menu['menu'] = inside_menu

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.win)
        self.widget = self.canvas.get_tk_widget()
        self.widget.place(relx=0, rely=0.2, relwidth=1, relheight=0.7)
        self.ax.scatter(self.feature, self.label, label=self.norm_menu['text'])
        self.canvas.draw()

    def change_plot(self, txt):
        self.norm_menu['text'] = txt
        # print(self.norm_menu['text'])
        if txt == self.normalization_options[0]:
            self.x_default()
        elif txt == self.normalization_options[1]:
            self.x_mean()
        else:
            print(txt)

    def x_default(self):
        self.ax.clear()
        self.ax.scatter(self.feature, self.label, label=self.norm_menu['text'])

        self.canvas.draw()

    def x_mean(self):
        x_max = max(self.feature)
        x_min = min(self.feature)
        x_new = []
        for val in self.feature:
            x_new.append((val-x_min)/(x_max-x_min))
        self.ax.clear()
        self.ax.scatter(x_new, self.label, label=self.norm_menu['text'])
        # self.ax.hist(x_new, bins=5)
        self.canvas.draw()

