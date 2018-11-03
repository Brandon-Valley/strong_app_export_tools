import tools
import export_format



export_filename = 'export.csv'
output_filename = 'correct_export.csv'

tools.export_to_csv(export_filename, output_filename)



row_dl = export_format.build_row_dict_list(export_filename)
print (row_dl)
# build_session_list(row_dl)


print('Done!')
