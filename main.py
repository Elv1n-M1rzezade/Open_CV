import cv2 as cv

capture = cv.VideoCapture("C:\\Users\\Elvin's\\Desktop\\Videos\\m2-res_1920p.mp4")
img = cv.imread("C:\\Users\\Elvin's\\Desktop\\Image\\download.jfif")

def rescaleFrame(frame,scale=0.5 ):

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width,height)

    return cv.resize(frame,dimension, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)



while True:
    isframe,frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video_resized',frame_resized)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


#
#
# resized_image = rescaleFrame(img)
# cv.imshow('Image',resized_image)
# cv.waitKey(0)