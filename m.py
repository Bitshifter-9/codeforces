dfs from 1 to compute subtree size sz[v] for each v;
for each edge (u,v) with parent u → v: s_e = min(sz[v], n – sz[v])
collect list L = [s_e for edges]
sort L ascending
# Let’s say we define increments when label(e) > something: we can compute for each possible “threshold” how many edges exceed it  
# then for target c, we sum over how many ways to pick those edges × ways to permute labels.
