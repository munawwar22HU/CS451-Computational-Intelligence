import math
import pprint
import time
import copy
from visualisation import output_image, Moves
# Using enum class create enumerations


class Reinforcement:
    def __init__(self, grid, discount=0.9, convergence=0.001):
        # Initialitize the reward and values matrix
        self.rewards = grid
        self.values = copy.deepcopy(grid)
        # self.policy = [[Moves.NoMove for i in range(10)] for j in range(10)]
        self.convergence = convergence
        self.discount = discount

    def getbestpolicy(self, i, j):
        # See all the possible moves and return the bestmove and its value
        moves = {Moves.Down: (i+1, j), Moves.Up: (i-1, j),
                 Moves.Left: (i, j-1), Moves.Right: (i, j+1)}
        validmoves = {}
        for move, end in moves.items():
            x, y = end
            if 0 <= x <= 9 and 0 <= y <= 9:
                validmoves[move] =  self.rewards[i][j] + self.discount * self.values[x][y]
        bestmove = max(validmoves, key=validmoves.get)
        return bestmove, validmoves[bestmove]

    def getpositions(self):
        # Returns positions whose value I have to update
        return [(x, y) for x in range(10) for y in range(10) if (self.values[x][y] == -1)]

    def run(self,filename,printwithoutpolicy=True):
        # Get the states, where I need to update values (not goal and not obstacle)
        states = self.getpositions()
        # While convergence is not reached
        notconverged = True
        while notconverged:
            maxchange = 0
            # Go through all states and update their values
            for x, y in states:
                # Get the old value
                oldvalue = self.values[x][y]
                # Find the best policy with highest value for next stage
                policy, value = self.getbestpolicy(x, y)
                self.values[x][y] = value
                maxchange = max(maxchange, abs(self.values[x][y] - oldvalue))
            notconverged = maxchange >= self.convergence
        # Generate policy
        policy = [[self.getbestpolicy(i,j)[0] if self.rewards[i][j] == -1 else Moves.NoMove for j in range(len(self.rewards[0]))] for i in range(len(self.rewards))]
        # Image generation
        output_image(filename, policy, self.rewards)
        if printwithoutpolicy:
            output_image(filename[:-4]+"_default.png",[[Moves.NoMove]*10]*10 , self.rewards)
        for i in self.values:
            print(i)
        return policy


grid1 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -100, -100, -100, -100, -1, -100],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -100, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -100, -100, -1, -1, -100, -100, -100, -1],
        [-1, -1, -100, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -100, -100, -100, -100, -100, -100, -100, 100]]

grid2 = [[100, -1, -1, -1, -1, -1, -1, -1, -1, 100],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [100, -1, -1, -1, -1, -1, -1, -1, -1, 100]]

grid3 = [[100, -100, -1, -1, -1, -1, -1, -1, -1, 100],
        [-1, -100, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -100, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -100, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -100, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -100, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [100, -1, -1, -1, -1, -1, -1, -1, -1, 100]]


grid4 = [[-100, -100, -1, -1, -1, -1, -1, -1, -1, -100],
        [-1, -100, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -100, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -100, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -100, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 100, -100, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-100, -1, -1, -1, -1, -1, -1, -1, -1, -100]]

test = Reinforcement(grid1)
policy = test.run("grid1.png")
test = Reinforcement(grid2)
policy = test.run("grid2.png")
test = Reinforcement(grid3)
policy = test.run("grid3.png")
test = Reinforcement(grid4)
policy = test.run("grid4.png")
