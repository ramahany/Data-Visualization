import tkinter as tk
import ttkbootstrap as ttk
from plt_data import PlotData
from Describe import Describe
import numpy as np
from ttkbootstrap.tableview import Tableview


class CreateNote:

    def __init__(self, frame: ttk.Frame, item: str, df, label, index, notebook):
        self.main_frm = frame
        # self.name = item
        self.df = df
        self.label = label
        self.tap_id = index
        self.Notebook = notebook
        num_rows = tuple([x for x in range(18)])
        num_columns = tuple([x for x in range(20)])

        self.main_frm.columnconfigure(num_columns, weight=1, uniform='a')
        self.main_frm.rowconfigure(num_rows, weight=1, uniform='a')
        # Create Widgets
        # feature Title
        feature_lbl = ttk.Label(self.main_frm, text=item, font=(None, 28, 'bold'), name='name_lbl',
                                bootstyle='primary', background='#FFFFFF', width=30)
        change_btn = ttk.Button(self.main_frm, text='Change Feature Name', name='change_name_btn',
                                command=lambda x=item: self.change_feature_name(x))
        # Notebook
        notebook_ntb = ttk.Notebook(self.main_frm, bootstyle='primary' , name='graph_ntb')
        scatter_frm = ttk.Frame(name=f'sctr_frm{index}')
        PlotData(self.df[[item, self.label]], scatter_frm, 'Scatter')
        hist_frm = ttk.Frame(name=f'hist_frm{index}')
        PlotData(self.df[[item, self.label]], hist_frm, 'hist')
        # Data
        datatbl_lblFrm = ttk.Labelframe(self.main_frm, text="Data", name='dataTable_lblFrm', bootstyle="Primary")
        # add data to the frame
        self.dt = None
        self.create_feature_tbl(datatbl_lblFrm, item)
        # Describe data
        data_char = ttk.Labelframe(self.main_frm, text="Data Characteristics ", name='dataChar_lblFrm',
                                   bootstyle="Primary")
        Describe(self.df[item], data_char)
        norm_frm = ttk.Labelframe(self.main_frm, text="Normalization", name='norm_lblFrm', bootstyle="Primary")
        # add to Notebook
        notebook_ntb.add(scatter_frm, text='Scatter')
        notebook_ntb.add(hist_frm, text='Histogram')
        # position widgets in page
        feature_lbl.grid(row=0, column=1, columnspan=3, rowspan=2, sticky='we')
        change_btn.grid(row=0, column=16, columnspan=3, rowspan=2, sticky='ew', ipady=15)
        notebook_ntb.grid(row=2, column=1, columnspan=7, rowspan=12, sticky='nsew')
        datatbl_lblFrm.grid(row=2, column=11, columnspan=8, rowspan=10, sticky='nsew', pady=21)
        data_char.grid(row=12, column=11, columnspan=8, rowspan=6, sticky='nsew', pady=21)
        norm_frm.grid(row=15, column=1, columnspan=7, rowspan=3, sticky='nsew', pady=21)

    def create_feature_tbl(self, frm: ttk.Labelframe, name):
        # name = frm.winfo_name().split('_tbl_frm')[0][1:] # get name
        self.dt = Tableview(
            master=frm,
            coldata=[name, self.label],
            rowdata=np.array(self.df[[name, self.label]]),
            paginated=True,
            searchable=False,
            bootstyle='dark',
            # stripecolor=(colors.light, colors.dark),
        )
        self.dt.pagesize = 30  # how meny records you want to show per page
        self.dt.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.98, relheight=0.98)

    def change_feature_name(self, name):

        def change_confirmed(old_name, new_name):
            if new_name != '':
                pass
                self.df = self.df.rename(columns={old_name: new_name})
                # DONE : update the label
                self.main_frm.children['name_lbl']['text'] = new_name
                # DONE : update the table in the note tap
                self.dt.configure(columns=[new_name, self.label])
                self.dt.destroy()
                self.create_feature_tbl(self.main_frm.children['dataTable_lblFrm'], new_name)
                # TODO : update the main table


                change_name_win.destroy()

        change_name_win = ttk.Toplevel(title='Change Feature Name', resizable=[False, False], alpha=.95 )
        change_name_win.geometry('800x400')
        # lbl
        change_lbl = ttk.Label(change_name_win, text=f'Change {name} to:', font=(None, 30, 'bold')
                               , bootstyle='primary')
        change_lbl.pack(fill='x', pady=20, padx=20)
        # Entry
        change_entry = ttk.Entry(change_name_win, font=(None, 24, 'bold')
                               ,bootstyle='primary')
        change_entry.pack(fill='x', pady=10, padx=30)
        # btn
        confirm_change_btn = ttk.Button(change_name_win, text='Confirm Title',bootstyle='secondary',
                                        command=lambda: change_confirmed(name, change_entry.get()))
        confirm_change_btn.pack(fill='x', pady=10, padx=30, ipady=10)
