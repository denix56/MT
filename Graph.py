class Graph(object):
    matrix = []
    catalog_cycles = {}

    def __init__(self, transaction_function={}):
        if transaction_function:
            vertices = list(transaction_function.values())
            for i in ['0', '1', ' ']:
                vertices.append((i, 'R', 'q1'))

            for vertex in vertices:
                for i in ['0', '1', ' ']:
                    state = (vertex[2], i)
                    if state in transaction_function:
                        self.matrix.append((vertex, transaction_function[state]))

    def DFScycle(self, u, endV, E, color, cycle):
        print(color[endV])
        if u != endV:
            color[u] += 1

        elif len(cycle) > 1 and color[endV] == 3:
            left = cycle[(len(cycle)-1) / 2][1]
            right =  cycle[len(cycle) / 2][1]
            if left != right and left != 'N' and right != 'N':
                cycle = cycle[:len(cycle) / 2]
                cycle.reverse()
                node = self.catalog_cycles
                for state in cycle:
                    node.setdefault(state, {})
                    node = node[state]
            return
        for w in E:
            if  w[0][2] == 'qs':
                return
            if w[1][2] == 'qs':
                continue
            if color[w[1]] < 3 and w[0] == u:
                cycle_new = list(cycle)
                cycle_new.append(w[1])
                self.DFScycle(w[1], endV, E, color, cycle_new)
                color[w[1]] = 1;

    def find_cycles(self):
        color = {}
        for i, _ in self.matrix:
            for k, _ in self.matrix:
                color[k] = 1
            cycle = [i]
            self.DFScycle(i, i, self.matrix, color, cycle)
        return self.catalog_cycles