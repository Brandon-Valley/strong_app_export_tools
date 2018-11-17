
BAR_WEIGHT = 45

def barbell___weight_correct(weight):
    return BAR_WEIGHT + (weight * 2)

def dumbell___weight_correct(weight):
    return weight * 2






WEIGHT_CORRECT_FUNC_D = {'"Squat (Barbell)"'          : barbell___weight_correct ,
                         '"Bench Press (Dumbbell)"'   : dumbell___weight_correct,
#                          '"Pull Up"'                  : None, 
#                          '"Deadlift (Barbell)"'       : None,
                         '"Bent Over Row (Dumbbell)"' : dumbell___weight_correct,
                         '"Overhead Press (Dumbbell)"': dumbell___weight_correct }
#                          '"Running"'                  : None}



def correct_weight(exercise_name, weight):
    for e_name, weight_correct_func in WEIGHT_CORRECT_FUNC_D.items():
        if exercise_name == e_name:
            return weight_correct_func(weight)
    return weight

# 
# if '"Squat (Barbell)"' in WEIGHT_CORRECT_FUNC_D.keys():
#     print ('yay')


import main
if __name__ == '__main__':
    main.main()