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

# get the number of problems per process
def get_ppps(ps, ns):
    ppps = []
    flat_ps = [item for sublist in ps for item in sublist]
    for i in range(len(ns)):
        ppps.append(ns[i]/flat_ps[i])
        #print("n: " + str(ns[i]) + " flat_p: " + str(flat_ps[i]))
    return sorted(list(set(ppps)))



ns, ps, times = get_data("./data_weak.txt", True) # get data from the batch result file
ppps = get_ppps(ps, ns)

# markers and linestyles
markers = ['o', 'v', 's', '<', '>', '8', 's', 'p', 'x']
lineStyles = ['-', '--', '-.', ':']
fig, ax = plt.subplots()

# plot the data
for i in range(len(ppps)):
    plt.loglog(ps[i], times[i], marker=markers[i%len(markers)], lineStyle=lineStyles[i%len(lineStyles)])
    #print("n = " + str(ns[i]) + " ps: " + str(ps[i]) + " ts: " + str(times[i]))

# set better labels for x and y axis
ax.set_xscale('log')
ax.set_xticks([1, 2, 4, 8, 16, 32, 64, 256])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_yscale('log')
ax.set_yticks([0.1, 1, 10, 100])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.grid(True)
plt.xlabel('#Processors')
plt.ylabel('Time [s]')
plt.legend([sc_notation(elem) for elem in ppps], loc='upper right', ncol=1, title='N')
plt.show()
