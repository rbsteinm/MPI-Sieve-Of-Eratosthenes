import matplotlib.pyplot as plt
from extract_data import *
import matplotlib

def sc_notation(n):
    exp = 0
    while(n >= 10):
        n  = n / 10
        exp = exp + 1
    if n % 1 == 0:
        n = int(n)
    return str(n) + "e+" + str(exp)

# Strong scaling
ns, ps, times = get_data("./data_strong.txt") # get data from the batch result file
markers = ['o', 'v', '^', '<', '>', '8', 's', 'p', 'x']

fig, ax = plt.subplots()

# plot the data
for i in range(len(ns)):
    plt.loglog(ps[i], times[i], marker=markers[i])
    #print("n = " + str(ns[i]) + " ps: " + str(ps[i]) + " ts: " + str(times[i]))
    print("n = " + str(ns[i]))
print("{:E}".format(1000000000000000))

# set better labels for x and y axis
ax.set_xscale('log')
ax.set_xticks([1, 2, 4, 8, 16, 32, 64, 256])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_yscale('log')
ax.set_yticks([0.1, 1, 10, 25, 50, 100, 200])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.grid(True)
plt.xlabel('#Processors')
plt.ylabel('Time [s]')
plt.legend([sc_notation(elem) for elem in ns], loc='upper right', ncol=1)
plt.show()
