import matplotlib.pyplot as plt

def paint(samples):
    xx = []
    yy = []
    for s in samples:
        xx.append(s[0])
        yy.append(s[1])

    fig = plt.figure()
    plt.plot(xx, yy, color='blue', marker='o', linestyle='None')
    plt.ylabel("x2")
    plt.xlabel("x1")
    # plt.savefig('data.png')
    plt.show()


