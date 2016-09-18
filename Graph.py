class Graph(object):
    matrix = []
    catalog_cycles = list()

    def __init__(self, transaction_function={}):
        if transaction_function:
            for key, value in transaction_function.items():
                for i in ['0', '1', ' ']:
                    if key[0] == value[2] and key[1] == i and value[1] != 'N':
                        continue
                    self.matrix.append((key, (value[2], i)))

    def DFScycle(self, u, endV, E, color, unavailableEdge, cycle):
        if u != endV:
            color[u] = 2
        elif len(cycle) > 1:
            self.catalog_cycles.append(cycle)
            return
        for w in E:
            if  w[0][0] == 'qs':
                return
            if w == unavailableEdge or w[1][0] == 'qs':
                continue
            if color[w[1]] == 1 and w[0] == u:
                cycle_new = list(cycle)
                cycle_new.append(w[1])
                self.DFScycle(w[1], endV, E, color, w, cycle_new)
                color[w[1]] = 1;

    def find_cycles(self):
        color = {}
        for i, _ in self.matrix:
            for k, _ in self.matrix:
                color[k] = 1
            cycle = [i]
            self.DFScycle(i, i, self.matrix, color, (), cycle)
        return self.catalog_cycles