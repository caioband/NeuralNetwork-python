from Matrix import Matrix
from PIL import Image




def ConvertDatatoMatrix(testValue=1):
    newMatrix = Matrix()
    im = Image.open('Images/Image.jpg')
    pixel_value = im.load()
    w,h = im.size
    newMatrix.rows = w
    newMatrix.cols = h
    print(w,h)
    for r in range(w+1):
        cols = []
        for c in range(h+1):
            cols.append(testValue) ## test value
        newMatrix.matrix.append(cols)

    newMatrix.__printMatrix__()



ConvertDatatoMatrix()