import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import csv

path = 'E:\\GANeratedHands_Release\\data\\withObject\\0001'
data = glob.glob(path + "\\*.png")[100:106]
joints = glob.glob(path + "\\*2D.txt")[100:106]


bidimensional_points = []
for joint in joints:
    with open(joint, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            bidimensional_points.append(','.join(row))


points = []
for bidim in bidimensional_points:
    points.append(bidim.split(','))


points_x = []
points_y = []
for point in points:
    points_x.append(point[::2])
    points_y.append(point[1::2])
print(len(points_x), len(points_y))


img = []
for _path in data:
    img.append(mpimg.imread(_path))
# print(type(img), len(img))

# fig, axes = plt.subplots(nrows=4, ncols=10, figsize=(50, 50))

for idx in range(len(img)):
    # img = PIL.Image.open(x)
    plt.subplot(2, 3, idx+1)
    plt.title(idx+1)
    plt.axis('off')
    plt.imshow(img[idx])
    plt.scatter(x=[points_x[idx]], y=[points_y[idx]], c='r', s=10)


plt.show()

