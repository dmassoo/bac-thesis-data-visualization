from sf_data_preparator import *
input_file_name = input('Type input file name:\n')
output_file_name = input('Type output file name:\n')
e = input('Show experimental data? True/False:\n')
begin_end_cleaner(input_file_name, output_file_name)
Lx1, Ly1, Ly2 = lists_of_values(output_file_name)


double_plotter(Lx1, Ly1, Lx1, Ly2, experimental=e, x_label='Wavelength, nm', y_label='D', window=71, poly_order=3,)
