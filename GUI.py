# https://dzone.com/articles/python-gui-examples-tkinter-tutorial-like-geeks
from tkinter import ttk
from tkinter import *

# Tabs
import Edit_Tab
import Blank_Tab



def build_gui(workout_database):    

    root = Tk()
    root.title("Strong Export Plotter")

    tab_control = ttk.Notebook(root)
    tab_control.grid(row=1, column=0, columnspan=999, rowspan=999, sticky='NESW')
    
    tab1 = Frame(tab_control)
    tab2 = Frame(tab_control)
    tab_control.add(tab1, text='Edit')
    tab_control.add(tab2, text='blank')

    tab_dict = {'edit': Edit_Tab.Edit_Tab(tab1, workout_database),
                'blank': Blank_Tab.Blank_Tab(tab2, workout_database)}
    
    #let all the tabs use each other's member variables
    for tab_name, tab in tab_dict.items():
        tab.tabs = tab_dict

    root.mainloop()





 
    
    
    
import main
if __name__ == '__main__':
    main.main()
    