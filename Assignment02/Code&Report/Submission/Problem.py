from Ant import *
class GraphColorACO:
    def __init__(self, q : int ,beta :  float ,alpha : float ,rho : float ,num_ants : int,num_iter : int):
        self.Q = q
        self.Beta = beta
        self.Alpha = alpha
        self.Rho = rho
        self.NumAnts = num_ants
        self.NumIter = num_iter
    def Initialize(self,filename):
        self.Graph = Graph(filename) 
        self.NumNodes = self.Graph.num_nodes
        self.Pheromone= np.ones((self.NumNodes,self.NumNodes))
        for i in range(self.NumNodes):
            for j in range(self.NumNodes):
                if self.Graph.graph[i][j] == 1:
                    self.Pheromone[i,j] = 0

        temp = [int(self.Graph.degree(i)) for i in range(self.NumNodes)]
        self.Colors = [i for i in range(1,max(temp)+1)]
        self.Ants = [Ant(self.Alpha,self.Beta,self.Q,self.Graph,self.Colors) for i in range(self.NumAnts)]
        self.Coloring = np.zeros(self.NumAnts)
    def GenerateSolution(self):
        for j in range(self.NumAnts):
            self.Ants[j].Initialize()
            self.Coloring[j] = self.Ants[j].CompleteTour(self.Pheromone)
    def UpdatePheromoneMatrix(self):
        Delta = np.zeros((self.NumNodes,self.NumNodes))
        for j in range(self.NumAnts):
            Delta = Delta + self.Ants[j].PheremoneMatrix()
        self.Pheromone =(self.Pheromone *(1- self.Rho)) + Delta
    def CurrentBest(self):
        return np.min(self.Coloring)
    def CurrentAverage(self):
        return np.mean(self.Coloring)
    
