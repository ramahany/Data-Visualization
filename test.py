import tkinter as tk
from tkinter import filedialog

import numpy as np
import pandas as pd
import ttkbootstrap as ttk


class NotebookMaker:

    children = []
    styles = {
        0: 'info',
        1: 'danger',
        2: 'success'
    }

    def __init__(self, win: ttk.window):
        self.Window = win
        self.Notebook = ttk.Notebook(self.Window, bootstyle=self.styles[0])
        self.create_children()
        self.Notebook.place(relx=0.5, rely=0.5, anchor='center', relheight=0.8, relwidth=0.8)

    def create_children(self):

        for i in range(3):
            frame = ttk.Frame()
            lbl = ttk.Label(frame, text=f'this is Frame number {i+1}'
                            , bootstyle=self.styles[i], font=('Times New Roman', 50, 'bold'))
            lbl.place(relx=0.5, rely=0.5, anchor='center', relheight=0.8, relwidth=0.8)
            self.Notebook.add(frame, text=f'this is frame num{i + 1}')


if __name__ == '__main__':

    df = pd.DataFrame({
        "A": [1,2,3,4],
        "B" : [5,6,7,8]
    })
    print(df)
    old_name, new_name = "A", "AAA"
    df = df.rename(columns={old_name: new_name})
    print(df)
    ar = np.array([1, 2, 3])
    print(ar.dtype)

