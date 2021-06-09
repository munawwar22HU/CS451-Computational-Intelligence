import numpy as np
import random
import bisect
import copy
import matplotlib.pyplot as plt
class Graph:
    def __init__(self,filename):
        f =  open(filename,'r')
        temp = f.readline().split()
        self.num_edges = int (temp[3])
        self.num_nodes = int (temp[2])
        self.graph = np.zeros((self.num_nodes,self.num_nodes))
       
        for x in f.readlines():
            x = x.split()
            if x[0] == 'e':    
                self.graph[int(x[1])-1][int(x[2])-1] = 1
                self.graph[int(x[2])-1][int(x[1])-1] = 1
    def neighbours(self,vertex,W=None):
        lst = np.arange(self.num_nodes)
        NW = list()
        for i in range(len(lst)):
            if self.graph[vertex][i] == 1 :
                NW.append(i)
        if W ==None:
            return set(NW)
        return set(NW).intersection(W)
    def degree(self,vertex,W = None):
        if W == None:
            return np.sum(self.graph[vertex])
        else:
            return len(set(self.graph[vertex]).intersection(W))


