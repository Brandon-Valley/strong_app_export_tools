import tools 
import arrow
import plot_tools
from twisted.test.raiser import raiseException




def graph_title(plot_type, exercise_names_l):
    graph_title = plot_type + ': ' + tools.de_quote_str( exercise_names_l[0] )
     
    
    for exercise_name in exercise_names_l[1:]:
        graph_title += ' vs. ' + tools.de_quote_str( exercise_name )
         
    return graph_title

    
    
#fix!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def graph_filename(graph_title):
#     GRAPH_FILENAME = 'max_reps_test' + arrow.now().format('YYYY-MM-DD') + '.html' # this works for some reason
    
#     date = arrow.now().format('YYYY-MM-DD')
#     print (date)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     print (graph_title)# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     a = 'Max Weight Squat (Barbell)'
#     filename = 'bbb_' + date + '___' + graph_title + '.html'
#     return filename
# #     title = str(g)
#     return arrow.now().format('YYYY-MM-DD')  + '.html' 
    return 'temp.html'
    

# this is a really bad and stupid way of doing things but I am lazy and ill fix it later
def get_trace(plot_type, wd,  exercise_name, correct_weight):
    if   plot_type == 'Max Weight':
        return wd.get_trace___max_weight(exercise_name, correct_weight)
    
    elif plot_type == 'Total Volume':
        return wd.get_trace___total_volume(exercise_name, correct_weight)
    
    elif plot_type == 'Max Reps':
        return wd.get_trace___max_reps(exercise_name, correct_weight)
    
    elif plot_type == 'Total Reps':
        return wd.get_trace___total_reps(exercise_name, correct_weight)
    
    else: 
        raiseException('invalid plot_type: ', plot_type)


def plot_data(kwargs):
#     tools.print_dict(kwargs)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
    
    title = graph_title(kwargs['plot_type'], kwargs['exercise_names_to_plot_l'])
    filename = graph_filename(title)
    
    
    if len(kwargs['exercise_names_to_plot_l']) > 1:
        trace_list = []
        for exercise_name in kwargs['exercise_names_to_plot_l']:
            trace_list.append(get_trace(kwargs['plot_type'], kwargs['workout_database'], exercise_name, kwargs['correct_weight']))
        plot_tools.plot_trace_list(title, filename, trace_list)
         
    else:
        trace = get_trace(kwargs['plot_type'], kwargs['workout_database'], kwargs['exercise_names_to_plot_l'][0], kwargs['correct_weight'])
        plot_tools.plot_single_trace(title, filename, trace)
     
    
def plot_workout_freq(wd):
    print('in plot_workout_freq')#1```````````````````````````````````````````````````````````````````````````````````````````````
    title = 'Workout Frequency'
    filename = graph_filename(title)
    
    trace = wd.get_trace___workout_freq()
    plot_tools.plot_single_trace(title, filename, trace)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import main
if __name__ == '__main__':
    main.main()