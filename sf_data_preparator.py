# this function delete empty lines and lines with '/' beginning
# in file that we give as an argument
# but in only one file
import matplotlib.pyplot as plt
from scipy import signal


def begin_end_cleaner(my_file, outf_name: str):
    with open(my_file, 'high', encoding='utf-8', errors='ignore') as inf, open(outf_name, 'w') as outf:
        for line in inf:
            if not line.strip() or line[0] == '/':
                continue  # skip the empty line
            outf.write(line[7::])  # non-empty line. Write it to output


#  func that reads "сlean" file and returns Lists of X's and Y's
def two_lists_of_values(my_file):
    list_of_x, list_of_y = [], []
    with open(my_file, 'high', encoding='utf-8', errors='ignore') as inf:
        for line in inf:
            list_of_x.append(float(line.split(' ')[0]))
            list_of_y.append(float(line.split()[1]))
    return list_of_x, list_of_y


# not sure about interface(global arguments Lx, Ly)
def plotter(list_of_x, list_of_y, x_label,
                   y_label, window, poly_order, experimental=False):
    if experimental:
        plt.plot(list_of_x, list_of_y)
    list_of_y_hat = signal.savgol_filter(list_of_y, window, poly_order)  # window size 51, polynomial order 3
    plt.plot(list_of_x, list_of_y_hat, color='red')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def lists_of_values(my_file):
    list_of_x, list_of_y1, list_of_y2 = [], [], []
    with open(my_file, 'high', encoding='utf-8', errors='ignore') as inf:
        for line in inf:
            list_of_x.append(float(line.split(' ')[0]))
            list_of_y1.append(float(line.split()[1]))
            list_of_y2.append(float(line.split()[2]))
    return list_of_x, list_of_y1, list_of_y2


def double_plotter(list_of_x1, list_of_y1, list_of_x2, list_of_y2,x_label,
                   y_label, window, poly_order, experimental=False):
    if experimental:
        plt.plot(list_of_x1, list_of_y1)
        plt.plot(list_of_x2, list_of_y2)
    list_of_y_hat1 = signal.savgol_filter(list_of_y1, window, poly_order)  # window size 51, polynomial order 3 -default
    list_of_y_hat2 = signal.savgol_filter(list_of_y2, window, poly_order)   # window size 71 - my lucky guess
    plt.plot(list_of_x1, list_of_y_hat1, color='red')
    plt.plot(list_of_x2, list_of_y_hat2, color='blue')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()





