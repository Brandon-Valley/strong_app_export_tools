import Set

class Exercise_Set_Block:
	def __init__(self, set_d):
		self.exercise_name = set_d['Exercise Name']
		self.notes         = set_d['Notes']
		self.weight_unit   = set_d['Weight Unit']
		self.set_list 	   = []
		
		self.add_set(set_d)
		
		
	def add_set(self, set_d):
		new_set = Set.Set(set_d)
		self.set_list.append(new_set)
		
	
				
	def print_me(self, indent = '  ', init_indent = ''):		
			print('')
			print(init_indent + 'Exercise_Set_Block: ')
			print(init_indent + indent + 'exercise_name: ' + self.exercise_name)
			print(init_indent + indent + 'notes:         ' + self.notes)
			print(init_indent + indent + 'weight_unit:   ' + self.weight_unit)
			
			print('')
			
			for set in self.set_list:
				set.print_me(indent, init_indent + indent *2)
	
	
	def max_weight(self):
		max_weight = 0
		
		for set in self.set_list:
			if set.weight > max_weight:
				max_weight = set.weight
		
		return max_weight
		
		
		
		
		
		
		
		
		





import main
if __name__ == '__main__':
    main.main()