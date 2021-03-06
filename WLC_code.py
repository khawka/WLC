
def modu1(G,N,res):
    m=0
    for  U in res:
        n=len(U);
        
        S=G.subgraph(U)
        
        rr=[]
        for kk in res:
            if not kk==U:
                rr.extend(kk)
        
        ov=list(set(U).intersection(set(rr)))
        
        sum1= 0
        i=0
        while i<len(U):
            j=i+1
            while j<len(U):
                if U[i] in ov :
                
                    
                    o=S.degree(U[i])
        
            
                    o1=0
                
                    for ll in res:
                        if U[i] in ll:
                            S1=G.subgraph(ll)
                            o1=o1+S1.degree(U[i])
                    
                    al1=o/o1
                else :   
                    al1=1
                     
                if  U[j] in ov  :
                    
                
                    oo=S.degree(U[j])                  
        
            
                    oo1=0
                    for ll in res:
                    
                        if U[j]in ll:
                            S1=G.subgraph(ll)
                            oo1=oo1+S1.degree(U[j]) 
                        
                    al2=oo/oo1   
                                
                else :   
                
                    al2=1
              
                
            
        
                #tt=2*cpt
            
               
                if G.has_edge(U[j],U[i]) :
                    x=((1-((G.degree(U[i])*G.degree(U[j]))/(2*N)))*al1*al2)
                    sum1= sum1+2*x  
                    
                else :
                    
                    
                    sum1= sum1+2*((0-((G.degree(U[i])*G.degree(U[j]))/(2*N)))*al1*al2)
                j=j+1
            i=i+1
        m=m+sum1

    m=m/(2*N)#compute the total modularity
    
    return(m)

def WLC(path,sep):
    #path: the path of txt file containing edges of graph
    # sep : the used separator in the file of edges
    import networkx as nx
    import time
    t=[]
    tri=[]
    
    #G=nx.read_gml(path)#GML file
    print('graph loading')
    G=nx.read_edgelist(path, comments='#', delimiter=sep, nodetype=int,encoding='utf-8')#txt file
    
    print('graph loading')
    
    
    ns=len(G.nodes())# number of nodes in G
    N=G.number_of_edges()# number of edges in G
    
    t=[]
    den=nx.density(G)
    
    re=[]
    res=[]
    res1=[]
    res2=[]
    rr=[]
    #
    w1=[]
    tps1= time.time()#
    T11=G.nodes()# list of nodes
    #Compute the clustering coeficient of nodes in G
    i=0
    while i<len(T11):
        cpt1=0
        xx=G.neighbors(T11[i])
        a=len(xx)
        j=0
        while j < a-1:
            j1=j+1
            while j1<a:
                if  G.has_edge(xx[j],xx[j1]):
                   cpt1=cpt1+1
                j1=j1+1
            j=j+1
        #aj=[cpt1,a]
        if a>1:
            w1.append(2*cpt1/(a*(a-1)))
        else:
            w1.append(0)
        i=i+1
    #print('b',w1)
    #w1 is the list of clustering coeficient of nodes in G
    T=G.nodes() #List of nodes in G
    while len(T)>0:
        nst=[]
        S=G.subgraph(T)# the subgraph of G containning elements in T
        for k in T:
            nst.append([S.degree(k),k])# list of nodes degrees in T 
    
        nst.sort(reverse=True) # sort of nodes degree 
        l=nst[0][1]# select the node with the highest node degree l
        print('processing of ',l)
        ini=list(set(S.neighbors(l)))# list of neighbors of l
        ini.append(l)#add l to its list of neighbor to construct the initial community
        n=len(ini)
        n1=len(ini)
        #print('ini',ini)
        b=True
        # the supprsion of nodes with weak ties with the elements in ini
        
        while b==True:
        
            
            m1=[]
            temp=-1
            for r in ini:
                
                a=w1[T11.index(r)]# the clustering coeficient of r
                x=S.neighbors(r)# the neighbors of r
                #print(x)
                ww1=0#the clustering coeficient and common_neighbors similarity of the set of neighbors of r
                ww2=0#the clustering coeficient and common_neighbors similarity of neighbors of r belonging to ini
                if len(x)>0:
                    for rr1 in x:
                        d1=w1[T11.index(rr1)]
                        d=(d1+len(sorted(nx.common_neighbors(G, r, rr1))))#/(len(G.neighbors(rr1))+len(x))
                        #print(d)
                        ww1=ww1+d
                        if rr1 in ini:
                            ww2=ww2+d
                    if ww1>0:
                        bl=ww2/ww1# the weighted belonging degree of r
                        #print(r,':',bl)
                        if bl<0.5:
                        
                            ini.remove(r)   #remove r from initial community if its weighted belonging degree <0.5                       
            
                    
                        
                        
            #print(n1)
            #ini= list(set(ini)-set(m1))
            n1=len(ini) # the new size of the initial community 
            if  n1<n:  
                n=n1        
                b=True
            else:
                b=False # stop when the size of the initial community remain stable    
        
        
        b=1
        print('expansion of community')
        while b==1:
            x=[]
            for k in ini:   
                x.extend(G.neighbors(k))
                x=list(set(x)-set(ini))
            #x is the list of neighbors of elements in the initial community
            n=len(ini)
            m1=[]
            for r in x:
                
                x1=G.neighbors(r)
                #print(x)
                ww1=0#the clustering coeficient and common_neighbors similarity of the set of neighbors of r
                ww2=0#the clustering coeficient and common_neighbors similarity of neighbors of r belonging to ini
                if len(x1)>0:
                    for rr1 in x1:
                        d1=w1[T11.index(rr1)]
                        d=(d1+len(sorted(nx.common_neighbors(G, r, rr1))))#
                        ww1=ww1+d
                        if rr1 in ini:
                            ww2=ww2+d
                    if ww1>0:
                        bl=ww2/ww1# the weighted belonging degree of r
                        
                        if bl>=0.4:
                        
                            m1.append(r)# select the node r as its belonging degree >0.4  
                                                  
                
                
            ini.extend(m1)# expand the initial community with the node having their  belonging degree >0.4   
            n1=len(ini)  # the new lenght of the community   
            if n1>n:
                b=1
                
            else:   
                 
                    b=0#stop when the size of the community remain stable  
                    
                    break                   
        
        
        res.append(ini)# load the community in the list of communities
        
        
        rr.extend(ini)# list of selected nodes
        T=list(set(T)-set(ini))# keep only unselected nodes in T
        
        
        if (len(ini)==0):
            T.remove(l) # when the resulted community is empty ignore the node l in the selection of the node with highest node strength
        
    
    
    #print(res)
    
    
    tps2= time.time()
    print('time',tps2-tps1)#the consumed time in the algorithm
    m=0 
    print("loading results in the file \'results\'")
    fichier = open("results.txt", "w")
    for res1 in res:
        for k in res1:
            fichier.write(str(k))
            fichier.write(' ')
        fichier.write('\n')
    fichier.close()
    #compute overlapping modularity
    m=modu1(G,N,res)
    print("the overlapping modularity is ",m)
  
   
    
