

class Set:
    def __init__(self, set_d):
        self.reps        = set_d['Reps']
        self.weight      = set_d['Weight']
        
#         self.seconds = set_d['seconds']
#         self.mi          = set_d['mi']
        
    def print_me(self, val_space = '  ', init_indent = ''):        
            print(init_indent + 'Set:' + val_space + 'weight: ' + self.weight + val_space + 'reps: ' + self.reps)

        
        
        
        
        
        
        
        
        



import main
if __name__ == '__main__':
    main.main()