import export_format
import tools
import Session

class Workout_Database:
    def __init__(self, export_filename):
        self.session_list = []
        
        
        self.build_session_list(export_filename)
        
        
    def build_session_list(self, export_filename):
        set_dl = export_format.build_row_dict_list(export_filename) # list of dicts, each dict represents a set
        print(set_dl)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        
        curr_date         = ''
        curr_workout_name = ''
        curr_session      = None
        
        for set_d in set_dl:
            tools.print_dict(set_d)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
            # decide if need to make new Session, if so, append curr_session and make new session, also set new curr_workout_name and curr_date
            if set_d['Date'] != curr_date or set_d['Workout Name'] != curr_workout_name:
                if curr_session != None:
                    self.session_list.append(curr_session)
                
                curr_session = Session.Session(set_d)
                curr_date         = set_d['Date']
                curr_workout_name = set_d['Workout Name']
                
                
    def print_me(self, indent = '    '):
        print('')
        print('')
        print('Workout_Database:')
        print(indent + 'num_sessions: ' + str( self.num_sessions() ))    
        
        for session_num, session in enumerate(self.session_list):
            session.print_me(indent, indent * 2, )
                
    
    def num_sessions(self):
        return len( self.session_list )
    
    
    def get_trace___max_weight(self, exercise_name):
        x = [] # date
        y = [] # weight
        
        for session in self.session_list.__reversed__():
            if exercise_name in session.exercise_name_set():
                x.append(session.date)
                y.append(session.max_weight(exercise_name))

























import main
if __name__ == '__main__':
    main.main()