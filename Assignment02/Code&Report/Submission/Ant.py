from Graph import *

class Ant:
    def __init__(self,Alpha : float , Beta :  float, Q : int , Graph, Colors):
        self.Graph = Graph                                      # Adjacency Matrix Representation
        self.Nodes = self.Graph.num_nodes                       # Number of nodes in the graph
        self.UnVisted = []                                      # Uncolored vertices 
        self.UnVisted = [i for i in range(self.Nodes)]          # Initialize the list of unvisted nodes

        self.Alpha = Alpha # Parameter Alpha
        self.Beta = Beta   # Parameter Beta
        self.Q = Q         # Parameter Q

        self.ColorsAvailaible = Colors     # Maximum number of Colors availaible
        self.Distance = 0                  # Number of colors used to color the graph
        self.ColorMapping = {}             # Mapping of Colors to a set of vertices
        self.ColorAssigned = dict()        # Mapping of each single vertice to a color
    def Initialize(self):

        for color in self.ColorsAvailaible:     # Initialize the mapping of colors to a set of vertices
            self.ColorMapping[color] = set()  
        for key in range(self.Graph.num_nodes): # Initialize the color assigned to each vertice
            self.ColorAssigned[key] = None    
    def SelectFirstNode(self,W : set ,B : set , Strategy : int):

        if Strategy == 1  :
            v = random.choice(list(W))
        elif Strategy == 2 :
            Degree = dict()  # Degree of each vertex:
            for w in W:
                Degree[w] = self.Graph.degree(w,W) 
            vertices  = list(Degree.keys())
            degrees = list(Degree.values())
            v = vertices[degrees.index(max(degrees))]
        return v
    def getDesirability(self,vertex,W,B,Strategy):
        if Strategy == 1:
            return self.Graph.degree(vertex,B)
        elif Strategy == 2:
            return self.Graph.degree(vertex,B.union(W))
        elif Strategy == 3:
            return len(W) - self.Graph.degree(vertex,W)
        
    def getPheremoneTrail(self,vertex,q,PheromoneMatrix):
        PheromoneSum = sum ([PheromoneMatrix[vertex][x] for x in self.ColorMapping[q]])
        return PheromoneSum / len(self.ColorMapping[q])
    def ComputeProbabilities(self,Desirability,PheromoneTrail,ListW):
        if not any(Desirability.values()):
            for v in Desirability:
                Desirability[v] = 1
        Numerator = np.zeros(len(ListW))
        for i in range(len(ListW)):
            Numerator[i] = (PheromoneTrail[ListW[i]]**self.Alpha)*(Desirability[ListW[i]]**self.Beta)
        Denominator = sum(Numerator)
        Probabilities = np.cumsum(Numerator/Denominator)
        Index = bisect.bisect_left(Probabilities,random.uniform(0,1))
        v = ListW[Index] 
        return v
    def CompleteTour(self,PheromoneMatrix):
    
        q = 0                   # number of colors used
        W = set(self.UnVisted)  # uncoloured vertices which can be included in the stable set under construction
        k = 0                   # number of coloured vertices

        while k < self.Nodes:
            k = k + 1 # Number of vertices Colored
            q = q + 1 # Number of Colors used
            B = set() # Uncolored vertices which can no longer belong to the stable set V_q
            
            v = self.SelectFirstNode(W,B,1)                  # Select the first node to be the given the color q 
            self.ColorMapping[q].add(v)                      # Add vertex v to the set of color q
            self.ColorAssigned[v] = q                        # Assign vertex v the color q 
            Neighbors = self.Graph.neighbours(v,W)  
            while len(W.difference(Neighbors.union({v})))>0: # W \ (N_w (v) U v) 
                k = k + 1                      
                B = B.union(Neighbors)          
                W = W.difference(Neighbors.union({v}))

                ListW = list(W) 
                Desirability = dict() 
                PheromoneTrail = dict() 
                Heuristic = dict() 
                Sum = 0

                for i in range(len(W)):
                    Desirability[ListW[i]] = self.getDesirability(ListW[i],W,B,2)
                    PheromoneTrail[ListW[i]] = self.getPheremoneTrail(ListW[i],q,PheromoneMatrix)

                
                v = self.ComputeProbabilities(Desirability,PheromoneTrail,ListW)
                Neighbors = self.Graph.neighbours(v,W)
                self.ColorMapping[q].add(v)
                self.ColorAssigned[v]=q
            W = B.union(Neighbors)
            
        self.Distance = q
        return self.Distance
    def PheremoneMatrix(self):
        PheromoneMatrix = np.zeros((self.Nodes,self.Nodes))
        for v1 in range(self.Nodes):
            for v2 in range(self.Nodes):
                if self.ColorAssigned[v1] == self.ColorAssigned[v2] and (v1!=v2):
                    PheromoneMatrix[v1,v2] = self.Q /self.Distance
        return PheromoneMatrix
        


        

