from Problem import *
class EA:
    def __init__(self, parent_selection_scheme, survivor_selection_scheme,pop_size = 30 , num_offspring = 10 , num_gen = 100, mutation_rate = 0.5 , num_iter = 10 ):

        self.pop_size = pop_size
        self.num_offspring = num_offspring
        self.num_gen = num_gen
        self.mutation_rate = mutation_rate
        self.num_iter = num_iter
        self.parent_selection_scheme = parent_selection_scheme
        self.survivor_selection_scheme = survivor_selection_scheme

    def initialize(self , problem: str , dataset: str ,is_random:bool , filename = ""):
        '''
        Initialize the Problem
        '''
        self.problem = problem(dataset) 
        self.is_random = is_random
        self.seedFileName = filename
        self.chromosomes = self.problem.generateChromosome(self.pop_size,is_random,filename)
        
    def Run(self):
        '''
        Run multiple generations of the problem
        '''
        for i in range(self.num_gen):
            self.RunGeneration()
            if i % 100 ==0:
                
                print(f"Generation {i+1}")
                self.problem.info(self.chromosomes)
    def RunGeneration(self):
        '''
        Run a single generation of the problem & update the values of the current generation , average fitness and best fitness 
        '''
        parents = self.problem.selection(self.num_offspring,self.chromosomes,self.parent_selection_scheme)
        for i in range(0,self.num_offspring,2):
            child = self.problem.recombine(parents[i],parents[i+1])
            self.problem.mutate(child,self.mutation_rate)
            self.chromosomes.extend(child)
            self.chromosomes = self.problem.survival(self.pop_size,self.chromosomes,self.survivor_selection_scheme)
    def AvgFitness(self):
        '''
        Compute avg fitness 
        '''
        return sum([self.problem.evaluateChromosomeFitness(chrom) for chrom in self.chromosomes])/len(self.chromosomes)
    
    def BestFitness(self):
        '''
        Compute best fitness 
        '''
        return max([self.problem.evaluateChromosomeFitness(chrom) for chrom in self.chromosomes])
    def SaveSolutions(self,filename):
        bestchromo = sorted(self.chromosomes , key= lambda item: item.evaluateFitness(self.problem.items), reverse=True)
        bestchromo = bestchromo[:]
        self.problem.saveGoodSolutions(bestchromo,filename)

    def RunAlt(self,filename):
        BSF = np.zeros((self.num_gen,self.num_iter))
        AVG = np.zeros((self.num_gen,self.num_iter))
        for i in range(self.num_iter): 
            self.chromosomes = self.problem.generateChromosome(self.pop_size,self.is_random,self.seedFileName)
            for j in range(self.num_gen):
                self.RunGeneration()
                BSF[j][i] = self.BestFitness()
                AVG[j][i] = self.AvgFitness()
        bsf_val = np.mean(BSF,axis=1)
        avg_val = np.mean(AVG,axis=1)
        BSF = np.column_stack((BSF,bsf_val))
        AVG = np.column_stack((AVG,avg_val))
        col_bsf = ['Run # '+str(i)+' BSF' for i in range(self.num_iter)] + ['Avg BSF']
        col_avg = ['Run # '+str(i)+' ASF' for i in range(self.num_iter)] + ['Avg ASF']
        df_avg = pd.DataFrame(AVG)
        df_avg.columns = col_avg
        df_bsf = pd.DataFrame(BSF)
        df_bsf.columns = col_bsf
        df_avg.to_csv(filename+"_AVG.csv")
        df_bsf.to_csv(filename+"_BSF.csv")
        



f = EA(RandomSelect(),BinaryTournamentSelect(),num_gen=10000,num_offspring=20,mutation_rate=0.80,num_iter=1)
f.initialize(TSPProblem,"DataSet/qa194.tsp",True)
f.RunAlt('rand_bt')