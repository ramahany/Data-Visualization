import numpy as np
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from read_data import get_data
from ttkbootstrap.tableview import Tableview
from features import NormalizeFeatures
from ttkbootstrap.scrolled import ScrolledFrame
from CreateNote import CreateNote


class DataVisualizationApp:

    def __init__(self, main_win: ttk.Window):
        self.window = main_win
        self.df = None
        self.label = None
        self.Notebook = ttk.Notebook(self.window, bootstyle='primary', name='features_ntb')
        self.main_frm = ttk.Frame()
        self.create_main_panel()
        self.Notebook.add(self.main_frm, text='Main')
        self.Notebook.pack(expand=True, fill='both')
        # self.Notebook.place(relx=0.5, rely=0.5, anchor='center', relheight=0.95, relwidth=0.95)

    def get_data_path(self):
        init_dir = 'D:\\! --♥\\projects\\automation\\data_visualization'
        title = 'Select csv file'
        file_types = (('text/csv', '*.csv'), ('all files', '*.csv'))
        file_path = filedialog.askopenfilename(initialdir=init_dir, title=title, filetypes=file_types)
        if file_path != '':
            self.df = get_data(file_path)
            # print(self.df.info())
            state = self.show_data()
            if state == -1:
                return
            self.build_note()
        return

    def show_data(self):


        temp = self.main_frm.children['data_frame']
        colors = self.window.style.colors

        test = self.chose_label()
        if test == 'None':
            self.df = None
            return -1
        else:
            self.label = test

        dt = Tableview(
            master=temp,
            coldata=self.df.columns.values,
            rowdata=np.array(self.df),
            paginated=True,
            searchable=False,
            bootstyle='dark',
            # stripecolor=(colors.light, colors.dark),
        )
        dt.pagesize = 30  # how meny records you want to show per page
        dt.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.98, relheight=0.98)
        self.main_frm.winfo_children()[0].winfo_children()[0].destroy()

        return

    def chose_label(self):

        def on_close():
            mini_win.destroy()

        mini_win = ttk.Toplevel(title='Chose Y(Label)', resizable=[False, False], alpha=.95)
        mini_win.geometry('800x400')
        mini_win.protocol("WM_DELETE_WINDOW", on_close)
        var = ttk.StringVar(value="None")
        lbl = ttk.Label(mini_win, textvariable=var)
        lbl.pack(pady=10)
        sf = ScrolledFrame(mini_win, autohide=True)
        sf.pack(fill='both', expand=True, padx=10, pady=10)
        for i in self.df.columns.values[1:]:
            btn = ttk.Button(sf, text=f'{i}', command=lambda x=i: var.set(x))
            btn.pack(fill='x', padx=20, ipady=20, pady=10)

        self.window.wait_window(mini_win)
        return var.get()
        # return ans


    def create_main_panel(self):
        num_rows = tuple([x for x in range(13)])
        num_columns = tuple([x for x in range(9)])

        self.main_frm.columnconfigure(num_rows, weight=1, uniform='a')
        self.main_frm.rowconfigure(num_columns, weight=1, uniform='b')

        data_frame = ttk.LabelFrame(self.main_frm, text='DATA',
                                    bootstyle="light.TLabelframe", name='data_frame')

        add_data_btn = ttk.Button(data_frame, text='Add Data', bootstyle="info",
                                  cursor='crosshair', width=50, command=self.get_data_path)

        add_data_btn.place(relx=0.5, rely=0.5, anchor='center', height=75)
        data_frame.grid(row=0, column=0, columnspan=13, rowspan=6, sticky='nsew', padx=30)

        # Create the eqn label frame
        eqn_frm = ttk.LabelFrame(self.main_frm, text='Regression Analysis'.upper(), bootstyle="light")
        train_btn = ttk.Button(self.main_frm, text='Train', bootstyle="info")
        eqn_frm.grid(row=7, column=0, columnspan=10, rowspan=1, sticky='nsew', padx=30)
        train_btn.grid(row=7, column=10, columnspan=3, rowspan=1, sticky='nsew', padx=30)
        return

    def build_note(self):
        features = self.df.columns.values[1:]
        index = 1
        for item in features:
            if item == self.label:
                continue
            temp_frm = ttk.Frame(name=f'mainFeature{index}_frm')
            # add to main Notebook
            CreateNote(temp_frm, item, self.df, self.label, index, self.Notebook)
            self.Notebook.add(temp_frm, text=item)
            index += 1









if __name__ == '__main__':
    window = ttk.Window(title='test place', themename="vapor",
                        resizable=[False, False], alpha=.95)
    window.geometry('1900x950')

    DataVisualizationApp(window)
    window.mainloop()
