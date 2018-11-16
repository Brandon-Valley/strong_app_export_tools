import tools
import export_format
import Workout_Database
import plot_tools
import GUI




export_filename = 'export.csv'
output_filename = 'correct_export.csv'




def main():
    print('converting export to correct CSV...')
    tools.export_to_csv(export_filename, output_filename)
    
    print('building workout database...')
    wd = Workout_Database.Workout_Database(export_filename) 

#     print(wd.exercise_names_list())#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
    print('starting gui...')
    GUI.build_gui(wd)
    
    print('Done!')





if __name__ == '__main__':
    main()