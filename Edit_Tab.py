from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import *

from tkinter import *

import Tab



class Edit_Tab(Tab.Tab):
    def __init__(self, master,wd):
        Tab.Tab.__init__(self, master)
        
        self.plot_type_____widget_setup()
        self.plot_btn_____widget_setup()
        
        self.grid_widgets()
        
    


    def plot_type_____widget_setup(self):
        self.plot_type  = StringVar()
        self.plot_type.set("max_weight") #default
        self.max_weight_rad_btn = Radiobutton(self.master,text='Max Weight  ', value='max_weight'  , variable = self.plot_type)
        self.total_vol_rad_btn  = Radiobutton(self.master,text='Total Volume', value='total_volume', variable = self.plot_type)
        self.max_reps_rad_btn   = Radiobutton(self.master,text='Max Reps     ', value='max_reps'    , variable = self.plot_type)
        self.total_reps_rad_btn = Radiobutton(self.master,text='Total Reps   ', value='total_reps'  , variable = self.plot_type)
 


    def plot_btn_____widget_setup(self):
        def plot_btn_clk():
            print('siudfhsiuhdfduhsouhfohdsolhfoihwsolrihfwolirhgoeihrgolehr')
            
            
            
        self.plot_btn = Button(self.master, text = 'PLOT', command = plot_btn_clk)

        
    def grid_widgets(self):
        blank_lbl = Label(self.master, text="") #for spacing 
        
        row_num = 10
        
        #output_background_color
        self.max_weight_rad_btn                .grid(column=1, row=row_num + 1, sticky=N+S+W)
        self.total_vol_rad_btn                 .grid(column=1, row=row_num + 2, sticky=N+S+W)
        self.max_reps_rad_btn                  .grid(column=1, row=row_num + 3, sticky=N+S+W)
        self.total_reps_rad_btn                .grid(column=1, row=row_num + 4, sticky=N+S+W)
        
        row_num += 10
#         
#         #background text color
#         self.bgnd_text_clr_lbl                  .grid(column=1, row=row_num)
#         self.bgnd_text_clr_tup_tb               .grid(column=2, row=row_num)
#         self.bgnd_text_clr_display_tb           .grid(column=3, row=row_num)
#         self.bgnd_text_clr_change_clr_btn       .grid(column=4, row=row_num)
#         
#         row_num += 10
#         
        blank_lbl                               .grid(column=1, row=row_num)
        
        row_num += 10
        
        self.plot_btn                           .grid(column=1, row=row_num)

        
#         
#         row_num += 10
#         
#         #input image background color
#         self.input_bgnd_clr_lbox                .grid(column=2, row=row_num)
#         self.input_bgnd_clr_sbar                .grid(column=3, row=row_num, sticky=N+S+W)
#         self.input_bgnd_clr_sel_btn             .grid(column=2, row=row_num + 1)
#         
#         self.input_bgnd_clr_tup_tb              .grid(column=4, row=row_num)
#         self.input_bgnd_clr_display_tb          .grid(column=5, row=row_num)
#         
#         self.trim_input_bgnd_clr_cbtn           .grid(column=2, row=row_num + 2)
#         























import main
if __name__ == '__main__':
    main.main()