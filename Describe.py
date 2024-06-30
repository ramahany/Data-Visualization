import numpy as np
import tkinter as tk
import ttkbootstrap as ttk
import pandas as pd
from pandas.api.types import is_numeric_dtype


class Describe:

    def __init__(self, data: pd.DataFrame, frame: ttk.LabelFrame):
        self.data = data
        self.frame = frame
        self.description = self.data.describe()
        self.type = self.get_type()
        type_lbl = ttk.Label(self.frame, text=self.type, font=(None, 32, 'normal'), bootstyle='secondary')

        if type_lbl == 'Categorical':

            self.show_description_for_categorical()
        else:
            self.show_description_for_numerical()

        type_lbl.pack()

    def get_type(self):
        return 'Categorical' if not is_numeric_dtype(self.data.dtypes) else 'Numeric'

    def show_description_for_numerical(self):
        print('Numerical')
        print(print(self.description))
        print('===============================')

    def show_description_for_categorical(self):
        print('Categorical')
        print(print(self.description))
        print('===============================')

