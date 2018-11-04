import export_format

class Workout_Database:
    def __init__(self, export_filename):
        self.session_list = None
        
        
        self.build_session_list(export_filename)
        
        
    def build_session_list(self, export_filename):
        row_dl = export_format.build_row_dict_list(export_filename)
        print (row_dl)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

























if __name__ == '__main__':
    import main
    main.main()