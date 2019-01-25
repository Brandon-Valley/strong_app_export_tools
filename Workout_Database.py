import export_format
import tools
import Session
import plot_tools

class Workout_Database:
    def __init__(self, export_filename):
        self.session_list = []
        
        
        self.build_session_list(export_filename)
        
        
    def build_session_list(self, export_filename):
        set_dl = export_format.build_row_dict_list(export_filename) # list of dicts, each dict represents a set
        
        for set_d in set_dl:
            
            # decide if need to make new Session, if so, append curr_session and make new session, also set new curr_workout_name and curr_date
            if (self.session_list                  == [] or
                self.session_list[-1].date         != set_d['Date'] or
                self.session_list[-1].workout_name != set_d['Workout Name']):
                
                new_session = Session.Session(set_d)
                self.session_list.append(new_session)
            
            else:
                self.session_list[-1].add_set(set_d)
                
                

    def print_me(self, indent = '    '):
        print('')
        print('')
        print('Workout_Database:')
        print(indent + 'num_sessions: ' + str( self.num_sessions() ))    
        
        for session_num, session in enumerate(self.session_list):
            session.print_me(indent, indent * 2, session_num)
                
                
    
    def num_sessions(self):
        return len(self.session_list)
    
    
    
    def exercise_names_list(self):
        exercise_names_l = []
        workout_names_s = set([])
        
        for session in self.session_list.__reversed__():
            if session.workout_name not in workout_names_s:
                workout_names_s.add(session.workout_name)
                exercise_names_l += session.exercise_names_list()
        return exercise_names_l
            
            
            
    def workout_names_list(self):
        workout_names_l = []
        
        for session in self.session_list.__reversed__():
            if session.workout_name not in workout_names_l:
                workout_names_l.append(session.workout_name)
        return workout_names_l
            
    
    def get_trace(self, trace_name, key, exercise_name, correct_weight, hover_info = True):
        x = [] # date
        y = [] # weight / reps / ect...
        hover_info_l = []
        
        for session in self.session_list.__reversed__():
            if exercise_name in session.exercise_names_list():
                x.append(session.date)
                
                if   key == 'max_weight':
                    y.append(session.max_weight(exercise_name, correct_weight))
                    
                elif key == 'total_volume':
                    y.append(session.total_volume(exercise_name, correct_weight))
                    
                elif key == 'max_reps':
                    y.append(session.max_reps(exercise_name))
                    
                elif key == 'total_reps':
                    y.append(session.total_reps(exercise_name))
                
                
                if hover_info == True:
                    hover_info_l.append(session.exercise_hover_info(exercise_name))        
                
        return plot_tools.default_trace(trace_name, x, y, hover_info_l)
    
    
    
    def get_trace___max_weight(self, exercise_name, correct_weight, hover_info = True ):
        trace_name = exercise_name + ':  Max Weight' 
        key = 'max_weight'
        return self.get_trace(trace_name, key, exercise_name, correct_weight, hover_info)


    def get_trace___total_volume(self, exercise_name, hover_info = True):
        trace_name = exercise_name + ':  Total Volume' 
        key = 'total_volume'
        return self.get_trace(trace_name, key, exercise_name, hover_info)
    

    def get_trace___max_reps(self, exercise_name, hover_info = True):
        trace_name = exercise_name + ':  Max Reps' 
        key = 'max_reps'
        return self.get_trace(trace_name, key, exercise_name, hover_info)
    
    
    def get_trace___total_reps(self, exercise_name, hover_info = True):
        trace_name = exercise_name + ':  Total Reps' 
        key = 'total_reps'
        return self.get_trace(trace_name, key, exercise_name, hover_info)
    
    
    def get_trace___workout_freq(self):
        print('in get_trace__workout_freq() in workout database, need to write new func for this')#``````````````````````````````````````````````````
























import main
if __name__ == '__main__':
    main.main()