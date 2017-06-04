# extract the data from the batch output file
def get_data(path, weak=False):

    ns = []
    ps = []
    ts = []

    data  = open(path, 'r')


    for line in data:
        if line[0] == 'n':
            n = ''
            p = ''
            t = ''
            i = 2
            while line[i].isdigit():
                n = n + line[i]
                i+=1
            while not line[i].isdigit():
                i+=1
            while line[i].isdigit():
                p = p + line[i]
                i+=1
            while not line[i].isdigit():
                i+=1
            #while i < len(line):
            while line[i].isdigit() or line[i] == '.':
                t = t + line[i]
                i+=1
            ns.append(int(n))
            ps.append(int(p))
            ts.append(float(t))
    if weak:
        # get the number of problems per process
        ppps = []
        for i in range(len(ns)):
            ppps.append(ns[i]/ps[i])
            #print("n: " + str(ns[i]) + " flat_p: " + str(flat_ps[i]))
        ppps = sorted(list(set(ppps)))
        elems_per_n = int(int(len(ts))/len(ppps))

    else:
        elems_per_n = int(len(ts) / len(set(ns)))
    ps_groups = [ps[i:i + elems_per_n] for i in range(0, len(ps), elems_per_n)]
    ts_groups = [ts[i:i + elems_per_n] for i in range(0, len(ts), elems_per_n)]
    return ns, ps_groups, ts_groups

#get_data("./data_strong.txt")