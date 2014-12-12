import cv2
cascPath = 'data/haarcascade_frontalface_default.xml'


def faces(imagepath):

    image = cv2.imread(imagepath)
    faceCascade = cv2.CascadeClassifier(cascPath)
    colorsforsquares = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return faceCascade.detectMultiScale(
        colorsforsquares,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
