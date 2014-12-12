from PIL import Image
from facecrap.utils.opencv import faces


def switcheroo(picture1, picture2):

    imgfaces = faces(picture1)
    (x1, y1, w1, h1) = imgfaces[0]
    imgfaces = faces(picture2)
    (x2, y2, w2, h2) = imgfaces[0]

    image1 = Image.open(picture1)
    image2 = Image.open(picture2)

    face1 = image1.transform((w2, h2), Image.EXTENT, (x1, y1, x1 + w1, y1 + h1))
    image2.paste(face1, (x2, y2, x2 + w2, y2 + h2))

    image2.show()
