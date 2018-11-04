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
        print(set_dl)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        for set_d in set_dl:
#             tools.print_dict(set_d)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
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
        return len( self.session_list )
    
    
    
    def get_trace___max_weight(self, exercise_name):
        name = exercise_name + ':  Max Weight' 
        x = [] # date
        y = [] # weight
        
        for session in self.session_list.__reversed__():
            if exercise_name in session.exercise_names_set():
                x.append(session.date)
                y.append(session.max_weight(exercise_name))
                
        return plot_tools.default_trace(name, x, y)


    def get_trace___volume(self, exercise_name):
        name = exercise_name + ':  Volume' 
        x = [] # date
        y = [] # weight
        
        for session in self.session_list.__reversed__():
            if exercise_name in session.exercise_names_set():
                x.append(session.date)
                y.append(session.volume(exercise_name))
                
        return plot_tools.default_trace(name, x, y)

























import main
if __name__ == '__main__':
    main.main()