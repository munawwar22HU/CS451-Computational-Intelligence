from Problem import *
class ACO:
    def __init__(self, q : int ,beta :  float ,alpha : float ,rho : float ,num_ants : int,num_iter : int):
        self.Q = q
        self.Beta = beta
        self.Alpha = alpha
        self.Rho = rho
        self.NumAnts = num_ants
        self.NumIter = num_iter
        self.BestFitnessSoFar = np.zeros(self.NumIter)
        self.AverageFitnessSoFar = np.zeros(self.NumIter)
    def Initialize(self,filename,Problem : str):
        if Problem == "GraphColor":
            self.Problem = GraphColorACO(self.Q,self.Beta,self.Alpha,self.Rho,self.NumAnts,self.NumIter)
            self.Problem.Initialize(filename)
    def Run(self):
        BestFitnessSoFar = float('inf')
        AverageFitnessSoFar = []
        for i in range(self.NumIter):
            self.Problem.GenerateSolution()
            self.Problem.UpdatePheromoneMatrix()
            AverageFitnessSoFar.append(self.Problem.CurrentAverage())
            self.AverageFitnessSoFar[i] = sum(AverageFitnessSoFar)/len(AverageFitnessSoFar)
       
            BestCurrentFitness = self.Problem.CurrentBest()
            if BestCurrentFitness < BestFitnessSoFar:
                BestFitnessSoFar = BestCurrentFitness
            self.BestFitnessSoFar[i] = BestFitnessSoFar
            
            print(f"Iteration {i}")
            print(f"Best Fitness So Far  :-  {round(BestFitnessSoFar,3)} ")
            print(f"Average Fitness So Far :- {round(self.AverageFitnessSoFar[i],3)}")
    def Plot(self,xlabel,ylabel,title):
        Iterations = [i for i in range(self.NumIter)]
        
        fig, (ax1,ax2) = plt.subplots(1, 2)
        ax1.plot(Iterations,self.BestFitnessSoFar,'tab:orange')
        ax1.set_xlabel(xlabel)
        ax1.set_title(title[0])
        ax1.set_ylabel(ylabel[1])
        ax2.plot(Iterations,self.AverageFitnessSoFar,'tab:green')
        ax2.set_xlabel(xlabel)
        ax2.set_title(title[1])
        ax2.set_ylabel(ylabel[1])
        plt.show()

            

AntColony=ACO(10,4,2,0.5,100,50)
AntColony.Initialize('data\gcol1.txt',"GraphColor")
AntColony.Run()
AntColony.Plot("Iterations",["Number of Color","Number of Color"],["Iterations vs Best Fitness so Far","Iterations vs Average Fitness so Far"])

"""
Strategy : {1,1}
Figure    =  1
Alpha     = 2
Beta      = 2
Rho       = 0.5
Nants     = 100
Ncycles   = 50
BFS       = 16
AFSF      = 17.923
"""


"""
Strategy : {1,2}
Figure    = 2
Alpha     = 2
Beta      = 4 
Rho       = 0.5
Nants     = 100
Ncycles   = 50
BFS       = 16
ASFS      = 17.481 
"""


"""
Strategy : {1,3}
Figure    = 3
Alpha     = 2
Beta      = 4 
Rho       = 0.5
Nants     = 100
Ncycles   = 50
BFS       = 16
ASFS      = 17.974



"""


"""
Strategy : {2,1}
Figure    = 4
Alpha     = 2
Beta      = 4 
Rho       = 0.5
Nants     = 100
Ncycles   = 50
BFS       = 18
ASFS      = 19.978
"""


"""
Strategy : {2,2}
Figure    = 5
Alpha     = 2
Beta      = 4 
Rho       = 0.5
Nants     = 100
Ncycles   = 50
BFS       = 18
ASFS      = 19.365
"""


"""
Strategy : {2,3}
Figure    = 6
Alpha     = 2
Beta      = 4 
Rho       = 0.5
Nants     = 100
Ncycles   = 50
BFS       = 17.0
ASFS      = 19.32
"""


"""
Vary alpha 
Strategy : {1,2}
Figure    = 7
Alpha     = 1
Beta      = 4 
Rho       = 0.5
Nants     = 100
Ncycles   = 50
BFS       = 18
ASFS      = 20.735

"""

"""
Vary beta 
Strategy : {1,2}
Figure    = 8
Alpha     = 2
Beta      = 2 
Rho       = 0.5
Nants     = 100
Ncycles   = 50
BFS       = 16
ASFS      = 17.632
"""

"""
Vary Rho 
Strategy : {1,2}
Figure    = 9
Alpha     = 2
Beta      = 4 
Rho       = 0.1
Nants     = 100
Ncycles   = 50
BFS       = 16
ASFS      = 19.402
"""

"""
Vary Ncycles 
Strategy : {1,2}
Figure    = 10
Alpha     = 2
Beta      = 4 
Rho       = 0.5
Nants     = 100
Ncycles   = 100
BFS       = 15
ASFS      = 16.718
"""

"""
Vary Nants 
Strategy : {1,2}
Figure    = 11
Alpha     = 2
Beta      = 4 
Rho       = 0.5
Nants     = 100
Ncycles   = 300
BFS       = 16
ASFS      = 17.101
"""

"""
Vary Q 
Strategy : {1,2}
Q = 10
Figure    = 2
Alpha     = 2
Beta      = 4 
Rho       = 0.5
Nants     = 100
Ncycles   = 50
BFS       = 16
ASFS      = 17.938
"""