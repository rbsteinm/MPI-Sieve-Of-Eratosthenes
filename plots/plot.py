import matplotlib.pyplot as plt
from extract_data import *
import matplotlib
# Strong scaling

ns, ps, times = get_data("./data_strong.txt") # get data from the batch result file

fig, ax = plt.subplots()

# plot the data
for i in range(len(ns)):
    plt.loglog(ps[i], times[i])
    #print("n = " + str(ns[i]) + " ps: " + str(ps[i]) + " ts: " + str(times[i]))
    print("n = " + str(ns[i]))

# set better labels for x and y axis
ax.set_xscale('log')
ax.set_xticks(ps[1])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_yscale('log')
ax.set_yticks([0.1, 1, 10, 25, 50, 100, 200])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.grid(True)
plt.xlabel('#Processors')
plt.ylabel('Time [s]')
plt.legend(ns, loc='upper left')
plt.show()

