from tkinter import *

import Tab

import plot_data
import tools



class Edit_Tab(Tab.Tab):
    def __init__(self, master, workout_database):
        Tab.Tab.__init__(self, master)
        
        self.workout_database = workout_database
        
        self.plot_type_____widget_setup()
        self.plot_btn_____widget_setup()
        
        self.grid_widgets()
        
    


    def plot_type_____widget_setup(self):
        self.plot_type  = StringVar()
        self.plot_type.set("Max Weight") #default
        self.max_weight_rad_btn = Radiobutton(self.master,text='Max Weight'   , value='Max Weight'  , variable = self.plot_type)
        self.total_vol_rad_btn  = Radiobutton(self.master,text='Total Volume' , value='Total Volume', variable = self.plot_type)
        self.max_reps_rad_btn   = Radiobutton(self.master,text='Max Reps'     , value='Max Reps'    , variable = self.plot_type)
        self.total_reps_rad_btn = Radiobutton(self.master,text='Total Reps'   , value='Total Reps'  , variable = self.plot_type)
 
 
        
    def exercise_____widget_setup_and_grid(self, row_num):
        self.exercise_sel_d = {}
        
        for i, exercise_name in enumerate(self.workout_database.exercise_names_list()):
            nq_exercise_name = tools.de_quote_str(exercise_name)
            
            exercise_cbtn_sel = IntVar(value = 0) #default to value
            exercise_cbtn = Checkbutton(self.master, text= nq_exercise_name, variable=exercise_cbtn_sel)
            
            exercise_cbtn.grid(column=1, row=row_num + i, sticky=N+S+W)
            
            self.exercise_sel_d[exercise_name] = exercise_cbtn_sel
        


    def plot_btn_____widget_setup(self):
        def plot_btn_clk():
            plot_kwargs = self.build_plot_kwargs()
            plot_data.plot_data(plot_kwargs)
        
        self.plot_btn = Button(self.master, text = 'PLOT', command = plot_btn_clk)

        
        
    def build_plot_kwargs(self):
        # make list of all exercise names to include in plot
        exercise_names_to_plot_l = []
        for exercise_name, cbtn_sel in self.exercise_sel_d.items():
            if cbtn_sel.get() == 1:
                exercise_names_to_plot_l.append(exercise_name)
        
        
        plot_kwargs = {'plot_type'               : self.plot_type.get(),
                       'workout_database'        : self.workout_database,
                       'exercise_names_to_plot_l': exercise_names_to_plot_l}
        
        return plot_kwargs
        
        
    def grid_widgets(self):
        blank_lbl_1 = Label(self.master, text="") #for spacing 
        blank_lbl_2 = Label(self.master, text="") #for spacing 
        
        row_num = 10
        
        #output_background_color
        self.max_weight_rad_btn                .grid(column=1, row=row_num + 1, sticky=N+S+W)
        self.total_vol_rad_btn                 .grid(column=1, row=row_num + 2, sticky=N+S+W)
        self.max_reps_rad_btn                  .grid(column=1, row=row_num + 3, sticky=N+S+W)
        self.total_reps_rad_btn                .grid(column=1, row=row_num + 4, sticky=N+S+W)
        
        row_num += 10

        blank_lbl_1                            .grid(column=1, row=row_num)
        
        row_num += 10
        
        self.exercise_____widget_setup_and_grid(row_num)
        
        row_num += 10
        
        blank_lbl_2                             .grid(column=1, row=row_num)
        
        row_num += 10
        
        self.plot_btn                           .grid(column=1, row=row_num)























import main
if __name__ == '__main__':
    main.main()