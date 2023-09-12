# main window

from tkinter import *
from tkinter import ttk
import tkinter as tk
import win32gui

options = []















def create_frame():
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)


root = Tk()
root.title("Energy Hack")

label = ttk.Label(root, text="Select an option:")
label.pack(pady=10)



selected_option = StringVar()  # Variable to hold the selected option
dropdown = ttk.Combobox(root, textvariable=selected_option, values=options, state="readonly")
dropdown.pack()



def add_option(new_option):
    if new_option:
        options.append(new_option)
        dropdown['values'] = tuple(options)




def get_window_location_and_size():
    global options

    def get_handles(hwnd, *args):
        if win32gui.GetWindowText(hwnd) == "METIN2" and hwnd not in options:  # check the title
            add_option(hwnd)
        return hwnd

    win32gui.EnumWindows(get_handles, None)

    print(options)

get_window_location_and_size()


def on_dropdown_select(event):
    selected_value = selected_option.get()
    print(f"Selected option: {selected_value}")
    get_window_location_and_size()

dropdown.bind("<<ComboboxSelected>>", on_dropdown_select)

#entry = ttk.Entry(root)
#entry.pack(pady=5)

#add_button = ttk.Button(root, text="Add Option", command=add_option)
#add_button.pack()

#frm = ttk.Frame(root, padding=10)
#frm.grid()
#ttk.Button(frm, text="Select window", command=create_frame).grid(column=1, row=0)

root.mainloop()
