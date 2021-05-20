import matplotlib.pyplot as plt
import random
import math
import method

samples = [[1,1], [1,2], [2, 3], [3, 1], [4, 1], [4, 5], [6,9], [6,7], [7, 10], [8, 10], [8, 9], [10, 8]]

def kmeans(c1, c2):
    global cluster1
    global cluster2

    cluster1 = []
    cluster2 = []

    for s in samples:
        distence_with_c1 = math.sqrt(((c1[0] - s[0]) ** 2) + ((c1[1] - s[1]) ** 2))
        distence_with_c2 = math.sqrt(((c2[0] - s[0]) ** 2) + ((c2[1] - s[1]) ** 2))

        # python 3.8
        # math.dist(c1, s)

        if distence_with_c1 <= distence_with_c2:
            cluster1.append(s)
        else:
            cluster2.append(s)


method.paint(samples)

lenth = len(samples)
r1 = random.randint(0,lenth-1)
r2 = random.randint(0,lenth-1)

while r1 == r2:
    r2 = random.randint(0,lenth)

centriod1 = samples[r1]
centriod2 = samples[r2]

print("initialization 1:", centriod1)
print("initialization 2:", centriod2)

cluster1 = []
cluster2 = []

isfirst = True
flag = True
lastcent = []

while flag:
    if isfirst:
        kmeans(centriod1, centriod2)
        lastcent = centriod1
        isfirst = False
    else:
        cluster1_x = []
        cluster1_y = []

        cluster2_x = []
        cluster2_y = []

        for x, y in cluster1:
            cluster1_x.append(x)
            cluster1_y.append(y)

        for x, y in cluster2:
            cluster2_x.append(x)
            cluster2_y.append(y)

        new_centriod1 = []
        new_centriod2 = []

        new_centriod1.append(sum(cluster1_x) / len(cluster1_x))
        new_centriod1.append(sum(cluster1_y) / len(cluster1_y))
        new_centriod2.append(sum(cluster2_x) / len(cluster2_x))
        new_centriod2.append(sum(cluster2_y) / len(cluster2_y))

        print("new centroid 1:", new_centriod1)
        print("new centroid 2:", new_centriod2)

        if set(lastcent) == set(new_centriod1):
            flag = False

        kmeans(new_centriod1, new_centriod2)
        lastcent = new_centriod1

plt.plot(cluster1_x, cluster1_y, color='blue', marker='o', linestyle='None')
plt.plot(cluster2_x, cluster2_y, color='red', marker='o', linestyle='None')
plt.ylabel("x2")
plt.xlabel("x1")
# plt.savefig('cluster1.png')
plt.show()
