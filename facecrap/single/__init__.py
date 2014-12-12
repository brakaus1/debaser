from random import randint
from PIL import Image
from facecrap.utils.opencv import faces


def cager(imagepath):

    imgfaces = faces(imagepath)

    ret = Image.open(imagepath)
    for face in imgfaces:
        caged(face[0], face[1], face[2], face[3], imagepath, ret)

    ret.show()

def caged(x, y, w, h, imagepath, ret):

    cage = Image.open('data/images/cage.jpg')
    cageresized = cage.resize((w, h))

    ret.paste(cageresized, (x, y, x + w, y + h))
