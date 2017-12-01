import networkx as nx
from itertools import *

rows = [line.strip() for line in open("24.txt", "r").readlines()]

nr,nc = len(rows),len(rows[0])
c = {}
G = nx.generators.classic.grid_2d_graph(nr,nc)
for i in range(nr):
  for j in range(nc):
    if rows[i][j]=='#':
      G.remove_node((i,j))
    if rows[i][j].isdigit():
      c[int(rows[i][j])] = (i,j)

d = {}
for i in range(len(c)):
  for j in range(len(c)):
    d[i,j]=d[j,i]= nx.shortest_path_length(G,c[i],c[j])

best = 10**100
for p in permutations(range(1,len(c))):
  l = [0] + list(p) + [0]
  t = sum(d[l[i+1],l[i]] for i in range(len(l)-1))
  best = min(t,best)
print(best)
