from Chromosome import *
from SelectionSchemes import *


class KnapSackItem:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


class KnapSackProblem:
    def __init__(self, filename: str):

        Data = open(filename, 'r')
        self.n, self.capacity = tuple(
            map(int, Data.readline().strip().split()))
        self.items: list[float] = []
        for i in range(self.n):
            value, weight = tuple(map(int, Data.readline().strip().split()))
            item = KnapSackItem(weight, value)
            self.items.append(item)

    def generateChromosome(self, pop_size: int,is_random : bool,filename = "") -> list:
        '''
        Return num amount of Chromosomes
        '''
        if is_random:

            return [KnapSackChromosome(self.capacity, self.n, False) for i in range(pop_size)]
        else:
            chromosomes = self.seedGoodSolutions(filename)
            temp = [KnapSackChromosome(self.capacity, self.n, False) for i in range(pop_size-len(chromosomes))]
            chromosomes.extend(temp)
        
            return chromosomes

    def evaluateChromosomeFitness(self, chromosome: KnapSackChromosome) -> float:
        '''
        Return Fitness Value
        '''
        return chromosome.evaluateFitness(self.items)

    def selection(self, how_many: int,Chromosomes, selection_scheme) -> list:
        '''
        return elements selected in an array
        '''
        return selection_scheme.ChromosomeChoose(Chromosomes,how_many,self)

    def survival(self, how_many: int, Chromosomes,selection_scheme) -> list:
        '''
        return elements that stay alive
        '''
        return selection_scheme.ChromosomeChoose(Chromosomes, how_many, self)

    def recombine(self, parent_1: KnapSackChromosome, parent_2: KnapSackChromosome) -> KnapSackChromosome:
        '''
        Does crossover and returns relevant chromosome
        '''
        a = copy.deepcopy(parent_1.allele)
        b = copy.deepcopy(parent_2.allele)
        a1 = a[:self.n//2]
        a2 = a[self.n//2:]
        b1 = b[:self.n//2]
        b2 = b[self.n//2:]
        return [KnapSackChromosome(self.capacity,self.n,True,a1+b2),KnapSackChromosome(self.capacity,self.n,True,b1+a2)]


    def mutate(self, chromosomes: list, probability: float) -> KnapSackChromosome:
        '''
        mutate every element in the list with certain probability
        '''
        for chromosome in chromosomes:
            if random.uniform(0,1) < probability:
                x = random.randint(0,self.n-1)
                if chromosome.allele[x] == 0:
                    chromosome.allele[x] = 1
                    
                elif chromosome.allele[x] == 1:
                    chromosome.allele[x] = 0
    def info(self,chromosomes):
        lst = [chrom.getProfit(self.items) for chrom in chromosomes]
        print(f"max value:{max(lst)}, avg value: {sum(lst)/len(lst)}")
    def saveGoodSolutions(self,chromosomes,filename):
        with open(filename,'wb') as filehandle:
            pickle.dump(chromosomes,filehandle,pickle.HIGHEST_PROTOCOL)
    def seedGoodSolutions(self,filename):
        with open(filename, 'rb') as f:
            chromosomes = pickle.load(f) 
            return(chromosomes)

        


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        # Other is City.
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def __str__(self):
        return f"{self.x} {self.y}"






class TSPProblem:
    def __init__(self, filename: str):

        # self.items: list[City] = []
        with open(filename) as f:
            final = [[float(x) for x in line.strip().split()[1:]]
                     for line in f.readlines()[7:-1]]
            self.items = [City(i, j) for i, j in final]
            self.length = len(self.items)

    def generateChromosome(self, num: int,is_random : bool,filename = ""):
        '''
        Return num amount of Chromosomes
        '''
        #return [TSPChromosome(self.length) for _ in range(num)]
        if is_random == True:
            return [TSPChromosome(self.length) for _ in range(num)]
        else:
            chromosomes = self.seedGoodSolutions(filename)
            temp = [TSPChromosome(self.length) for _ in range(num)]
            chromosomes.extend(temp)
            return chromosomes

    def evaluateChromosomeFitness(self, chromosome: TSPChromosome) -> float:
        '''
        Return Fitness Value
        '''
        return chromosome.evaluateFitness(self.items)

    def selection(self, how_many: int, Chromosomes, selection_scheme):

        '''
        return elements selected in an array
        '''
        return selection_scheme.ChromosomeChoose(Chromosomes, how_many, self)

    def survival(self, how_many: int, Chromosomes, selection_scheme):
        '''
        return elements that stay alive
        
        '''
        return selection_scheme.ChromosomeChoose(Chromosomes, how_many, self)

    def recombine(self, parent_1: TSPChromosome, parent_2: TSPChromosome) -> TSPChromosome:
        '''
        # Does crossover and returns relevant chromosome
        '''
        return [TSPChromosome.generateFromParents(parent_1, parent_2, self.length), TSPChromosome.generateFromParents(parent_2, parent_1, self.length)]

    def mutate(self, chromosomes, probability: float) -> TSPChromosome:
        '''
        mutate every element in the list with certain probability
        '''
        for chromosome in chromosomes:
            if random.uniform(0,1) < probability:
                x, y = random.randint(0,self.length-1),random.randint(0,self.length-1)
                chromosome.allele[x],chromosome.allele[y] = chromosome.allele[y],chromosome.allele[x] 
    def info(self,chromosomes):
        lst = [chrom.getDistance(self.items) for chrom in chromosomes]
        mindst = min(lst)
        avgdist = sum(lst)/len(lst)
        print(f"min dist:{mindst}, avg dist: {avgdist}")
        return mindst,avgdist
        
    def saveGoodSolutions(self,chromosomes,filename):
        with open(filename,'wb') as filehandle:
            pickle.dump(chromosomes,filehandle,pickle.HIGHEST_PROTOCOL)
    def seedGoodSolutions(self,filename):
        with open(filename, 'rb') as f:
            chromosomes = pickle.load(f) 
            return(chromosomes)
