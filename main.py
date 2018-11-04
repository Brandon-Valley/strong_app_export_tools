import tools
import export_format
import Workout_Database


export_filename = 'export.csv'
output_filename = 'correct_export.csv'






def main():
    tools.export_to_csv(export_filename, output_filename)
    
    wd = Workout_Database.Workout_Database(export_filename) 
    
    
    #print (row_dl)
    # build_session_list(row_dl)
    
    print('num sessions: ', wd.num_sessions())
    print('last sesh exersise names: ', wd.session_list[-1].exercise_names_set())
    
    wd.print_me()#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    print('Done!')





if __name__ == '__main__':
    main()