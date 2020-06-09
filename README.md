# WLC


The algorithm of "A new local algorithm for overlapping community detection based on clustering coefficient and common neighbour similarity" is uploaded in WLC_code file.
the required package is networkx 

The function WLC  inputs are: path: the path of txt file containing edges of graph
    sep : the used separator in the file of edges

The Output: is the file results that contain overlapping communities

 Run this function in python3.4 using: 
 import WLC_code as WLC
 f='edges-file-name.txt'
 WLC.WLC(f,',')
 
Citation: Asmi, K., Lotfi, D., & El marraki, M. (2019, March). A new local algorithm for overlapping community detection based on clustering coefficient and common neighbor similarity. In Proceedings of the ArabWIC 6th Annual International Conference Research Track (pp. 1-6).
