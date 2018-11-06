import export_format
import logger



def export_to_csv(export_filename, output_filename):
   row_dict_list = export_format.build_row_dict_list(export_filename)
   logger.logList(row_dict_list, output_filename, True)



def print_dict(dict):
	print('{')
	for key, value in dict.items():
		print('%s: %s' %(key, value))
	print('}')
	
	
	
# ('hi', 4) = 'hi  '
def add_spaces_for_min_length(str, min_length):
# 	if len(str) < min_length:
# 		return str + ' ' * (1 + min_length - len(str))
# 	else:
# 		return str

	while(len(str) < min_length):
		str += ' '
	return str
	
	


import main
if __name__ == '__main__':
    main.main()