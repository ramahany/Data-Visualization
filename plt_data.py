import pandas as pd
import numpy as np
import tkinter as tk
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas.api.types import is_numeric_dtype


class PlotData:

    def __init__(self, df: pd.DataFrame, frm: ttk.Frame, plot_type: str):
        self.df = df
        self.x = self.df.columns[0]
        self.y = self.df.columns[1]
        # if not is_numeric_dtype(self.df[self.x]) or is_numeric_dtype(self.df[self.y]) or self.x == self.y:
        #     return

        self.plot_type = plot_type
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=frm)
        self.widget = self.canvas.get_tk_widget()
        self.widget.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.95, relheight=0.95)
        self.update_plot()
        plt.close(self.fig)

    def update_plot(self, event=None):
        if self.df is not None:

            self.ax.clear()

            if self.plot_type == 'hist':
                # Calculate the number of bins using the Sturges' rule
                try:

                    if not is_numeric_dtype(self.df[self.x].dtype):
                        u = self.df[self.x].unique()
                        plt.xticks(range(len(u)), u, rotation='vertical')
                        num_bins = len(u)
                    else:
                        num_bins = int(np.ceil(np.log2(len(self.x))) + 1)
                    # Create histogram counts, bins, patches =
                    self.ax.hist(self.df[self.x].replace(pd.NA, 'Unknown'), bins=num_bins, edgecolor='black', label='distribution')

                except Exception as ex:
                    print(ex)

            elif self.plot_type == 'Scatter':
                if not is_numeric_dtype(self.df[self.x].dtype):
                    try:
                        self.ax.bar(self.df[self.x].replace(pd.NA, 'Unknown'), self.df[self.y], label=f'{self.y} vs {self.x}',
                                    color='purple', width=0.5, edgecolor='black', lw=1)
                        u = self.df[self.x].unique()
                        plt.xticks(range(len(u)), u, rotation='vertical')
                        self.ax.set_ylabel(self.y)

                    except Exception as ex:
                        print(f"An exception occurred at {self.x}\n and the exception is: {ex}")

                else:
                    self.ax.scatter(self.df[self.x], self.df[self.y], label=f'{self.y} vs {self.x}')
                    self.ax.set_ylabel(self.y)

            self.ax.set_xlabel(self.x)

            self.ax.legend()

            # #Set y-axis limits (if needed)
            # # plt.ylim(0, 100)
            #
            # #Use logarithmic scale (if needed)
            # plt.yscale('log')
            plt.tight_layout()
            self.canvas.draw()
