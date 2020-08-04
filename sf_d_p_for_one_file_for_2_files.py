from sf_data_preparator import *

input_file_name1 = input('Type input file1 name:\n')
input_file_name2 = input('Type input file2 name:\n')
output_file_name1 = input('Type output file1 name:\n')
output_file_name2 = input('Type output file2 name:\n')
e = input('Show experimental data? True/False:\n')
begin_end_cleaner(input_file_name1, output_file_name1)
begin_end_cleaner(input_file_name2, output_file_name2)
Lx1, Ly1 = two_lists_of_values(output_file_name1)
Lx2, Ly2 = two_lists_of_values(output_file_name2)


double_plotter(Lx1, Ly1, Lx1, Ly2, experimental=e, x_label='Wavelength, nm', y_label='D', window=71, poly_order=3,)