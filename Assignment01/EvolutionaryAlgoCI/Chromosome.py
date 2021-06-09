import bisect
import copy
import math
import random
import pickle
import more_itertools as mit
import numpy as np 
from random import choices
import pandas as pd 

class TSPChromosome:
    def __init__(self, num_cities: int):
        self.allele = list(mit.random_permutation(range(num_cities)))
        self.num_cities: int = num_cities

    def evaluateFitness(self, cities):
        # Compute Distance and return reciprocal
        distance = self.getDistance(cities)
        return(1/distance)

    def getDistance(self, cities):
        distance = sum([cities[city].distance(
            cities[(self.allele[(i+1) % self.num_cities])]) for i, city in enumerate(self.allele)])
        return distance
    def __str__(self):
        return f"{self.allele}"

    @classmethod
    def generateFromParents(self, parent_1, parent_2, length):
        onethird = length//3
        twothird = (length*2)//3

        a = TSPChromosome(length)
        # a.allele = [-1] * length

        a.allele[onethird:twothird] = parent_1.allele[onethird:twothird]
        elA = set(parent_1.allele[onethird:twothird])
        i = twothird
        j = twothird
        # Do till all elements not put
        while len(elA) < length:

            elToAdd = parent_2.allele[j]
            j = (j+1) % length
            if elToAdd not in elA:
                a.allele[i] = elToAdd
                elA.add(elToAdd)
                i = (i+1) % length
        return a

class KnapSackChromosome:
    def __init__(self, capacity: int, n: int, ischild: bool, allele: list = []) -> list:
        self.capacity = capacity
        self.n = n
        if not ischild:
            self.allele = [random.randint(0, 1) for _ in range(n)]
        else:
            self.allele = allele

    def evaluateFitness(self, items):
       
        return self.getProfit(items)
    def getProfit(self,items):
        value = 0
        if self.getWeight(items) <= self.capacity:
          
            for i in range(self.n):
                if self.allele[i] :
                    value = value + items[i].value
        return value

    def getWeight(self,items):
        weight = 0
        for i in range(self.n):
            if self.allele[i] :
                weight = weight + items[i].weight
        return weight


    def __str__(self):
        return f"{self.allele}"
    def __repr__(self):
        return str(self)

