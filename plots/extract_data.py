def get_data(path):

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
    elems_per_n = int(len(ts) / len(set(ns)))
    print(elems_per_n)
    #print(len(set(ns)))
    #print(len(ts))
    ps_groups = [ps[i:i + elems_per_n] for i in range(0, len(ps), elems_per_n)]
    ts_groups = [ts[i:i + elems_per_n] for i in range(0, len(ts), elems_per_n)]
    #print(ts_groups)
    print(set(ns))

    return sorted(list(set(ns))), ps_groups, ts_groups

#get_data("./data_strong.txt")