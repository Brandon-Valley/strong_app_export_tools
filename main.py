import tools
import export_format
import Workout_Database
import plot_tools

import arrow

export_filename = 'export.csv'
output_filename = 'correct_export.csv'






def main():
    tools.export_to_csv(export_filename, output_filename)
    
    wd = Workout_Database.Workout_Database(export_filename) 
    
    
    #print (row_dl)
    # build_session_list(row_dl)
    
    print('num sessions: ', wd.num_sessions())
    print('last sesh exersise names: ', wd.session_list[-1].exercise_names_list())
    print('all exercise names: ', wd.exercise_names_list())
    print('workout names: ', wd.workout_names_list())
    
#     wd.print_me()#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    GRAPH_TITLE = 'max weight vs vol test'
    GRAPH_FILENAME = 'max_weight_test' + arrow.now().format('YYYY-MM-DD') + '.html'
      
    trace1 = wd.get_trace___max_weight('"Squat (Barbell)"')
    plot_tools.plot_single_trace(GRAPH_TITLE, GRAPH_FILENAME, trace1)

#     GRAPH_TITLE = 'vol test'
#     GRAPH_FILENAME = 'vol_test' + arrow.now().format('YYYY-MM-DD') + '.html'
#     
#     trace2 = wd.get_trace___total_volume('"Squat (Barbell)"')
#     plot_tools.plot_single_trace(GRAPH_TITLE, GRAPH_FILENAME, trace2)

#     plot_tools.plot_trace_list(GRAPH_TITLE, GRAPH_FILENAME, [trace1, trace2])
    
    
    
    
    
    print('Done!')





if __name__ == '__main__':
    main()