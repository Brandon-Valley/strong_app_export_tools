import logger
import tools

export_delim = ';'


def make_row_dict(raw_row_dict, header_list):
   correct_row_dict = {}

   value_str = list(raw_row_dict.values())[0]
   value_list = value_str.split(export_delim)

   for val_num in range( len(value_list) ):
      correct_row_dict[header_list[val_num]] = value_list[val_num]

   return correct_row_dict


def build_row_dict_list(export_filename):
   row_dl = []
   raw_input = logger.readCSV(export_filename)

   #get header list
#    headers_str = raw_input[0].keys()[0]
   headers_str = list(raw_input[0].keys())[0]
   header_list = headers_str.split(export_delim)
   #print(header_list)

   for raw_row_dict in raw_input:
      row_dict = make_row_dict(raw_row_dict, header_list)
      row_dl.append(row_dict)

   return row_dl
