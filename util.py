import numpy as np


class AMath:
    def __init__(self):
        return
    def sigmoid(self,x):
        return 1/(1+ np.exp(-x))


class ImageUtils:
    def __init__(self):
        return

    def RGBToSingleValue(self, RGBTuple):
        r = RGBTuple[0]
        g = RGBTuple[1]
        b = RGBTuple[2]

        return (r+g+b)/3
    def RGBSingleZeroToOne(self, single):
        return single/255