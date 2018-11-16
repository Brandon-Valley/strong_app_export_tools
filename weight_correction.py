
BAR_WEIGHT = 45

def squat_barbell___weight_correct(weight):
    return BAR_WEIGHT + (weight * 2)



# a = {'v': squat___weight_correct}
#     
# print (a['v'](5))




WEIGHT_CORRECT_FUNC_D = {'"Squat (Barbell)"'          : squat_barbell___weight_correct ,
                         '"Bench Press (Dumbbell)"'   : None,
                         '"Pull Up"'                  : None, 
                         '"Deadlift (Barbell)"'       : None,
                         '"Bent Over Row (Dumbbell)"' : None,
                         '"Overhead Press (Dumbbell)"': None,
                         '"Running"'                  : None}



def correct_weight(exercise_name, weight):
    for e_name, weight_correct_func in WEIGHT_CORRECT_FUNC_D.items():
        if exercise_name == e_name:
            return weight_correct_func(weight)

# 
# if '"Squat (Barbell)"' in WEIGHT_CORRECT_FUNC_D.keys():
#     print ('yay')


import main
if __name__ == '__main__':
    main.main()