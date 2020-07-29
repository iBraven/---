import glob
import csv

path = "D:\\DSUsers\\UIC82704\\GANeratedHands_Release\\data"


def format_data(file):
    formated = file.read()
    formated = formated.split(",")
    formated[-1] = formated[-1][:-1]
    return formated


def make_csv(img_name, pos):
    # field_names = ['nume_img', 'W', 'T0', 'T1', 'T2', 'T3', 'I0', 'I1', 'I2', 'I3', 'M0', 'M1', 'M2', 'M3', 'R0', 'R1', 'R2', 'R3', 'L0', 'L1', 'L2', 'L3']
    with open('test.csv', 'a', newline='') as csvfile:
        writer_csv = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)

        for i in range(len(img_name)):
            f = open(pos[i], 'r')
            data = format_data(f)

            writer_csv.writerow([img_name[i] + ',' + ','.join(data)])


def iter_dir(_path):
    dir_names = glob.glob(_path + "\\*")
    for _dir in dir_names:
        name_img = glob.glob(_dir + "\\*.png")
        name_pos = glob.glob(_dir + "\\*joint_pos.txt")
        print(_dir)
        make_csv(name_img, name_pos)


# iter_dir(path)
# def iter_directory(_path):
#     dir_names = glob.glob(_path + "\\*")
#     for _dir in dir_names:
#         if os.path.isdir(_dir):
#             print(_dir)
#             iter_directory(_dir)
#         # else:
#             # name_img = glob.glob(dir + "\\*.png")
#             # name_pos = glob.glob(dir + "\\*joint_pos.txt")
#             # print(_dir)
#             # make_csv(name_img, name_pos)

iter_dir(path + '\\noObject')
iter_dir(path + '\\withObject')

