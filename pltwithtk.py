import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CVSPlotter:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('CSV Plotter')
        self.root.geometry('600x600')

        self.plot_types = ('Line Plot', 'Bar Plot', 'Scatter Plot')
        self.plot_type_var = tk.StringVar()  # set default to Line Plot

        # plot_menu = tk.OptionMenu(self.root, self.plot_type_var, *self.plot_types, command=self.update_plot)
        plot_menu = ttk.OptionMenu(self.root, self.plot_type_var, 'Line Plot',  *self.plot_types,
                                   command=self.update_plot)
        plot_menu.place(relx=0, rely=0.01, relwidth=0.6, relheight=0.1)

        load_button = ttk.Button(self.root, text='Load data', command=self.load_csv)
        load_button.place(relx=0.61, rely=0.01, relwidth=(1-0.61), relheight=0.1)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.widget = self.canvas.get_tk_widget()
        self.widget.place(relx=0, rely=0.15, relwidth=1, relheight=0.8)

        self.df = None

    def load_csv(self):
        init_dir = 'D:\\! --♥\\projects\\automation\\data_visualization'
        title = 'Select csv file'
        file_types = (('text/csv', '*.csv'), ('all files', '*.csv'))
        file_path = filedialog.askopenfilename(initialdir=init_dir, title=title, filetypes=file_types)
        if file_path != '':
            self.df = pd.read_csv(file_path)
            # print(len(self.df.columns.values))
            self.update_plot()

    def update_plot(self, event=None):

        if self.df is not None:
            plot_type = self.plot_type_var.get()
            x = self.df.columns[0]
            y = self.df.columns[1]

            self.ax.clear()

            if plot_type == 'Line Plot':
                self.ax.plot(self.df[x], self.df[y], label=f'{y} vs {x}')
            elif plot_type == 'Bar Plot':
                self.ax.bar(self.df[x], self.df[y], label=f'{y} vs {x}')
            elif plot_type == 'Scatter Plot':
                self.ax.scatter(self.df[x], self.df[y], label=f'{y} vs {x}')

            self.ax.set_xlabel(x)
            self.ax.set_ylabel(y)
            self.ax.legend()
            self.canvas.draw()


if __name__ == '__main__':
    window = tk.Tk()
    CVSPlotter(window)
    window.mainloop()
