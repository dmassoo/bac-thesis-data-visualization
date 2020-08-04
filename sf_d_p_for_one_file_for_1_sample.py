from sf_data_preparator import *

input_file_name1 = input('Type input file name:\n')
output_file_name1 = input('Type output file name:\n')
e = input('Show experimental data? True/False:\n')
begin_end_cleaner(input_file_name1, output_file_name1)
begin_end_cleaner(input_file_name1, output_file_name1)
Lx1, Ly1 = two_lists_of_values(output_file_name1)


plotter(Lx1, Ly1, experimental=e, x_label='Wavelength, nm', y_label='D', window=71, poly_order=3)
