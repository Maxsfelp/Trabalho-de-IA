import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def cliques(G):
    if len(G) == 0:
        return

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = [None]

    subg = set(G)
    cand = set(G)
    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    stack = []

    try:
        while True:
            if ext_u:
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q
                adj_q = adj[q]
                subg_q = subg & adj_q
                if not subg_q:
                    yield Q[:]
                else:
                    cand_q = cand & adj_q
                    if cand_q:
                        stack.append((subg, cand, ext_u))
                        Q.append(None)
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                Q.pop()
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass

if __name__ == '__main__':
    G = nx.Graph()

    G.add_nodes_from(range(0, 64))

    for x_i in range(0,8):
        for y_i in range(0,8):
            for x_j in range(0,8):
                for y_j in range(0,8):
                    if(x_i != x_j or y_i != y_j):
                        if(x_i == x_j or y_i == y_j or abs(x_i - x_j) == abs(y_i - y_j)):
                            G.add_edge(x_i + y_i * 8, x_j + y_j * 8)

    j = 0
    GC = nx.complement(G)
    for i in cliques(GC):
        if len(list(i)) == 8:
            j = j + 1
            print(i)

    print('São', j,'possbilidades')

    nx.draw(G, with_labels=True, font_weight='bold', width=1)
    plt.show()
    nx.draw(GC, with_labels=True, font_weight='bold', width=1)
    plt.show()