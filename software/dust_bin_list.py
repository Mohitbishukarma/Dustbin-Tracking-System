from tkinter import Canvas
import tkinter as tk
from tkinter import ttk
def make_dust_bin_list_view(parent_frame:str) -> None:
    def add_dustbin():
        ...


    # Create a Treeview with 5columns columns
    tree = ttk.Treeview(parent_frame, columns=("column1", "column2", "column3", "column4"))
    # Set the heading for each column
    tree.heading("#0", text="S.N")
    tree.heading("#1", text="Code")
    tree.heading("#2", text="Address")
    tree.heading("#3", text="Location")
    tree.heading("#4", text="Type")

    # Add data to the table from data file
    with open("data_files/dust_bins_info.txt", mode="rt", encoding="utf-8") as dust_bins:
        list_of_dust_bins = dust_bins.read().split("\n")[:-1]
        for index,each_dust_bin in enumerate(list_of_dust_bins):
            dust_bin = each_dust_bin.split(",,")
            tree.insert("","end",text=dust_bin[0], values=(dust_bin[1], dust_bin[2],dust_bin[3],dust_bin[4]))

    # Configure the column widths
    tree.column("#0", width=40, minwidth=45,stretch=tk.NO, )
    tree.column("#1", width=150, minwidth=150, stretch=tk.NO)
    tree.column("#2", width=150, minwidth=150, stretch=tk.NO)
    tree.column("#3", width=150, minwidth=150, stretch=tk.NO)
    tree.column("#4", width=150, minwidth=150, stretch=tk.NO)

    # Enable sorting when the user clicks on a column header
    tree.bind("<Button-1>", lambda event: tree.focus_set())
    tree.bind("<Button-1>", lambda event: tree.heading("#0", text="S.N", command=lambda:sort_column("#0", False)))
    tree.bind("<Button-1>", lambda event: tree.heading("#1", text="Code", command=lambda: sort_column("#1", False)))
    tree.bind("<Button-1>", lambda event: tree.heading("#2", text="Address", command=lambda: sort_column("#2", False)))
    tree.bind("<Button-1>", lambda event: tree.heading("#3", text="Location", command=lambda: sort_column("#3", False)))
    tree.bind("<Button-1>", lambda event: tree.heading("#4", text="Type", command=lambda: sort_column("#3", False)))

    # Add the Treeview to the window
    tree.pack( expand=0, pady=0)

    add_dustbin_btn = tk.Button(parent_frame,text="Add New Dustbin", command=add_dustbin())
    add_dustbin_btn.pack()