import glob
import csv

path = "D:\\DSUsers\\UIC82704\\GANeratedHands_Release\\data"
field_names = ['nume_img',
                   'Wx', 'Wy', 'Wz',
                   'T0x', 'T0y', 'T0z',
                   'T1x', 'T1y', 'T1z',
                   'T2x', 'T2y', 'T2z',
                   'T3x', 'T3y', 'T3z',
                   'I0x', 'I0y', 'I0z',
                   'I1x', 'I1y', 'I1z',
                   'I2x', 'I2y', 'I2z',
                   'I3x', 'I3y', 'I3z',
                   'M0x', 'M0y', 'M0z',
                   'M1x', 'M1y', 'M1z',
                   'M2x', 'M2y', 'M2z',
                   'M3x', 'M3y', 'M3z',
                   'R0x', 'R0y', 'R0z',
                   'R1x', 'R1y', 'R1z',
                   'R2x', 'R2y', 'R2z',
                   'R3x', 'R3y', 'R3z',
                   'L0x', 'L0y', 'L0z',
                   'L1x', 'L1y', 'L1z',
                   'L2x', 'L2y', 'L2z',
                   'L3x', 'L3y', 'L3z']

def format_data(file):
    formated = file.read()
    formated = formated.split(",")
    formated[-1] = formated[-1][:-1]
    return formated


def make_csv(_path, field):
    with open('test.csv', 'a', newline='') as csvfile:
        writer_csv = csv.writer(csvfile, delimiter = ' ', quoting=csv.QUOTE_MINIMAL)
        writer_csv.writerow(','.join(field))

        class_dir = glob.glob(_path + "\\*")
        class_dir
        for dirs in class_dir:
            for _dir in glob.glob(dirs + "\\*"):
                img_name = glob.glob(_dir + "\\*.png")
                pos = glob.glob(_dir + "\\*joint_pos.txt")
                print(_dir)
                for i in range(len(img_name)):
                    f = open(pos[i], 'r')
                    data = format_data(f)

                    writer_csv.writerow([img_name[i] + ',' + ",".join(data)])


def iter_dir(_path):
    dir_names = glob.glob(_path + "\\*")
    for _dir in dir_names:
        name_img = glob.glob(_dir + "\\*.png")
        name_pos = glob.glob(_dir + "\\*joint_pos.txt")
        print(_dir)




make_csv(path, field_names)

