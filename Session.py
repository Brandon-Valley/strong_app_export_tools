import Exercise_Set_Block

#contains all Exersise_Set_Blocks for that workout 
class Session:
    def __init__(self, set_d):
        self.date                      = set_d['Date']
        self.workout_name            = set_d['Workout Name']
        
        self.exercise_set_block_list = []
        
        
        self.add_set(set_d)
        
        
    def add_set(self, set_d):
        
        # decide if new exercise_set_block needs to be made, if so, makes it and appends to end of self.exercise_set_block_list
        if (self.exercise_set_block_list == [] or 
            self.exercise_set_block_list[-1].exercise_name != set_d['Exercise Name']):
            
            new_esb = Exercise_Set_Block.Exercise_Set_Block(set_d)
            self.exercise_set_block_list.append(new_esb) 
        
        else:
            self.exercise_set_block_list[-1].add_set(set_d)
            
            
    def print_me(self, indent = '  ', init_indent = '', session_num = ''):        
            print('')
            print(init_indent + 'Session: ' + session_num)
            print(init_indent + indent + 'date:         ' + self.date)
            print(init_indent + indent + 'workout_name: ' + self.workout_name)
            
            for esb in self.exercise_set_block_list:
                esb.print_me(indent, init_indent + indent * 2)
            
            
            
            
    def exercise_names_set(self):
        exercise_name_s = set({})
        
        for esb in self.exercise_set_block_list:
            exercise_name_s.add(esb.exercise_name)
            
        return exercise_name_s
    
    
    
                 

















import main
if __name__ == '__main__':
    main.main()