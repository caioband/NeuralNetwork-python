import math
from numpy.random import rand

from Matrix import Matrix
def Uniform_Weight_Initialization(inputAmount, outputAmount):
    return -1/math.sqrt(inputAmount), 1/math.sqrt(outputAmount)

class Neural:
    def __init__(self, inputAmount=None, outputAmount=None, outputModel=None):
        if not outputModel:
            raise Exception("outputModel not found")
        self.inputAmount = inputAmount
        self.outputAmount = outputAmount
        self.outputModel = outputModel
        self.totalWeights = inputAmount * outputAmount + outputAmount
        self.weights = []

        for input in range(inputAmount):
            Whandler = []
            for nextlayer in range(outputAmount):
                r1, r2 = Uniform_Weight_Initialization(inputAmount,outputAmount)
                numbers = rand(1000)
                scaled = r1 + numbers * (r1-r2)
                Whandler.append(scaled)
            self.weights.append(Whandler)

        for bias in range(outputAmount):
            print("a")
            r1,r2 = Uniform_Weight_Initialization(inputAmount,outputAmount)
            numbers = rand(1000)
            scaled = r1 + numbers * (r1-r2)
            self.weights.append(scaled)


    def GetoutputValue(self, outputName):
        return self.outputModel[outputName]

