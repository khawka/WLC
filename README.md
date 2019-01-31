# WLC


The algorithm of "A new local algorithm for overlapping community detection based on clustering coefficient and common neighbour similarity" is uploaded in file WLC code.

The function WLC  inputs are: path: the path of txt file containing edges of graph
    sep : the used separator in the file of edges

The Output: is the file results containing overlapping communities

 Run this function in python using: 
 import WLC_code as WLC
 f='karate.txt'
 WLC.WLC(f,',')
 the required package is networkx 
