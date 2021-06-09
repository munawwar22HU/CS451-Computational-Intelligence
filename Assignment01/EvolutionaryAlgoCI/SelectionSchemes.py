from Chromosome import *

# class SelectScheme(metaclass = abc.ABCMeta):
#     @abc.abstractmethod
#     def ChromosomeChoose(self,Chromosomes,n):
#         pass
class FitnessProportionSelect:
    def ChromosomeChoose(self,Chromosomes,n,Problem):
        lst = []
        chrom = []
        length = len(Chromosomes)
        for i in range(length):
            lst.append(Chromosomes[i].evaluateFitness(Problem.items))
        lst = np.array(lst)
        lst = lst / np.sum(lst)
        lst = np.cumsum(lst)
        for i  in range(n):
            chrom.append(Chromosomes[bisect.bisect_left(lst, random.uniform(0,1))])
        return chrom



class RankBasedSelect:
    def ChromosomeChoose(self,Chromosomes,n,Problem):
        chrom = []
        Chromosomes = sorted(Chromosomes , key= lambda item: item.evaluateFitness(Problem.items))
        # for chrom in SortedChromo:
        #     print(chrom.evaluateFitness(Problem.items))
        length = len(Chromosomes)
        lst = np.arange(1,length+1)
        lst = lst / np.sum(lst)
        lst = np.cumsum(lst)
        for i  in range(n):
            r = random.uniform(0,1)
            chrom.append( Chromosomes[(bisect.bisect_left(lst,r )) ])
        return chrom
        
class BinaryTournamentSelect:
    def ChromosomeChoose(self,Chromosomes,n,Problem):
        chrom = []
        length = len(Chromosomes)
        indices = choices(range(length), k = 2*n)
        for i in range(0,2*n,2):
            a,b = Chromosomes[indices[i]],Chromosomes[indices[i+1]]
            a_fit = a.evaluateFitness(Problem.items)
            b_fit = b.evaluateFitness(Problem.items)
            if a_fit > b_fit:
                chrom.append(Chromosomes[indices[i]])
            else:
                chrom.append(Chromosomes[indices[i+1]])
        return chrom
        
class TruncationSelect:
    def ChromosomeChoose(self,Chromosomes,n,Problem):
        bestchromo = sorted(Chromosomes , key= lambda item: item.evaluateFitness(Problem.items), reverse=True)
        bestchromo = bestchromo[:n]
        return bestchromo
class RandomSelect:
    def ChromosomeChoose(self,Chromosomes,n,Problem):
        return choices(Chromosomes,k=n)