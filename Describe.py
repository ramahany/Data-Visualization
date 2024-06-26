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
        lbl = ttk.Label(frame, text=str(self.description)+f'==>>>{self.type}')
        lbl.place(relx=0.5, rely=0.5, anchor='center')

    def get_type(self):
        return 'Categorical' if not is_numeric_dtype(self.data.dtypes) else 'Numeric'
