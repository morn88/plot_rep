import random
import matplotlib.pyplot as plt

fig = plt.figure()
def creat_plot():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        xy.append(y)
    return xs, ys

ax1 = fig.add_subplot(1, 1, 1)