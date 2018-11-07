import tools 
import arrow
import plot_tools
from twisted.test.raiser import raiseException




def graph_title(plot_type, exercise_names_l):
#     graph_tile = ''
    graph_title = plot_type + ': ' + tools.de_quote_str( exercise_names_l[0] )
     
    
    for exercise_name in exercise_names_l[1:]:
        graph_title += ' vs. ' + tools.de_quote_str( exercise_name )
         
    return graph_title

#     return 'sdoihfoidhosihfo' # fix !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    
    
def graph_filename(graph_title):
#     date = arrow.now().format('YYYY-MM-DD')
#     filename = date + '___' + graph_title + '.html'
#     return filename
    return 'vol_test' + arrow.now().format('YYYY-MM-DD') + '.html' #fix!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    

# this is a really bad and stupid way of doing things but I am lazy and ill fix it later
def get_trace(plot_type, exercise_name, wd):
    if   plot_type == 'Max Weight':
        return wd.get_trace___max_weight(exercise_name)
    
    elif plot_type == 'Total Volume':
        return wd.get_trace___total_volume(exercise_name)
    
    elif plot_type == 'Max Reps':
        return wd.get_trace___max_reps(exercise_name)
    
    elif plot_type == 'Total Reps':
        return wd.get_trace___total_reps(exercise_name)
    
    else: 
        raiseException('invalid plot_type: ', plot_type)


def plot_data(kwargs):
    tools.print_dict(kwargs)
    
#     kwargs['workout_database'].print_me()#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    
    title = graph_title(kwargs['plot_type'], kwargs['exercise_names_to_plot_l'])
#     print (title) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    filename = graph_filename(graph_title)
    
    
    if len(kwargs['exercise_names_to_plot_l']) > 1:
        trace_list = []
        for exercise_name in kwargs['exercise_names_to_plot_l']:
            trace_list.append(get_trace(kwargs['plot_type'], exercise_name, kwargs['workout_database']))
        plot_tools.plot_trace_list(title, filename, trace_list)
        
    else:
        trace = get_trace(kwargs['plot_type'], kwargs['exercise_names_to_plot_l'][0], kwargs['workout_database'])
        print(trace.y) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        plot_tools.plot_single_trace(title, filename, trace)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import main
if __name__ == '__main__':
    main.main()