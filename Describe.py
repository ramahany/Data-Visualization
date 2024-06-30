import numpy as np
import tkinter as tk
import ttkbootstrap as ttk
import pandas as pd
from pandas.api.types import is_numeric_dtype


class Describe:

    def __init__(self, data: pd.DataFrame, frame: ttk.LabelFrame):
        self.data = data
        self.frame = frame
        self.frame.grid_propagate(False)
        self.description = self.data.describe()
        self.type = self.get_type()
        rows = [x for x in range(10)]
        self.frame.rowconfigure(rows, weight=1, uniform='c')
        type_lbl = ttk.Label(self.frame, text=f'{self.type}: ({str(self.data.dtypes)})', font=(None, 14, 'bold'), bootstyle='primary')
        type_lbl.grid(row=0, column=1, sticky='nsew', padx=20)
        if self.type == 'Categorical':
            self.show_description_for_categorical()
        else:
            self.show_description_for_numerical()

    def get_type(self):
        return 'Categorical' if not is_numeric_dtype(self.data.dtypes) else 'Numeric'

    def show_description_for_numerical(self):

        index = 1
        for key in self.description.keys():
            print(key)
            lbl = ttk.Label(self.frame, text=f'{key}: {self.description[key]}',  font=(None, 11, 'bold'))
            lbl.grid(row=index, column=1, sticky='nsew', padx=70)
            index += 1

    def show_description_for_categorical(self):
        index = 1
        for key in self.description.keys():
            lbl = ttk.Label(self.frame, text=f'{key}: {self.description[key]}', font=(None, 11, 'bold'))
            lbl.grid(row=index, column=1, sticky='nsew', padx=70)
            index += 1

