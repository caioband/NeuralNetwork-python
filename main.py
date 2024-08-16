from Matrix import Matrix
from PIL import Image
from util import AMath
from util import ImageUtils
from Neural import Neural as N
import Neural

iu = ImageUtils()
im = Image.open('Images/Image.jpg')

def ConvertPixelsDatatoMatrix(im):
    newMatrix = Matrix()
    px = im.load()
    w,h = im.size
    newMatrix.rows = w
    newMatrix.cols = h
    for r in range(w):
        cols = []
        for c in range(h):
            rgbValue = px[r,c]
            rgbValue = iu.RGBToSingleValue(rgbValue)
            rgbValue = iu.RGBSingleZeroToOne(rgbValue)
            cols.append(rgbValue)
        newMatrix.matrix.append(cols)

    newMatrix.__debugMatrix__()
    return newMatrix


MatrixObject = ConvertPixelsDatatoMatrix(im)
outputModel = {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0,"5": 0,"6": 0,"7": 0,"8": 0,"9": 0,}

StartNeural = N(MatrixObject.rows*MatrixObject.cols, len(outputModel), outputModel)
WeightsMatrix = Matrix(StartNeural.inputAmount, StartNeural.outputAmount,StartNeural.weights)

print(StartNeural.inputAmount, StartNeural.outputAmount)

##WeightsMatrix.__printMatrix__()

##WeightsMatrix.__debugMatrix__()


print(StartNeural)
