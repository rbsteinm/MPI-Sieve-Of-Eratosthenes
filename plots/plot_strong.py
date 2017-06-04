import matplotlib.pyplot as plt
from extract_data import *
import matplotlib

# convert a number into a string of its scientific notation
def sc_notation(n):
    exp = 0
    while(n >= 10):
        n  = n / 10
        exp = exp + 1
    if n % 1 == 0:
        n = int(n)
    return str(n) + "e+" + str(exp)

# get data from the batch output file
ns, ps, times = get_data("./data_strong.txt")
ns = sorted(list(set(ns)))

# markers and linestlyes
markers = ['o', 'v', '^', '<', '>', '8', 's', 'p', 'x']
lineStyles = ['-', '--', '-.', ':']
fig, ax = plt.subplots()

# plot the data
for i in range(len(ns)):
    plt.loglog(ps[i], times[i], marker=markers[i%len(markers)], lineStyle=lineStyles[i%len(lineStyles)])
    #print("n = " + str(ns[i]) + " ps: " + str(ps[i]) + " ts: " + str(times[i]))

# set better labels for x and y axis
ax.set_xscale('log')
ax.set_xticks([1, 2, 4, 8, 16, 32, 64, 256])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_yscale('log')
ax.set_yticks([0.1, 1, 10, 25, 50, 100, 200])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

# set grid and legend
plt.grid(True)
plt.xlabel('#Processors')
plt.ylabel('Time [s]')
plt.legend([sc_notation(elem) for elem in ns], loc='upper right', ncol=1, title='N')
plt.show()
