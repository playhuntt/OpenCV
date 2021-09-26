import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)


# Reading Image
img = cv.imread('Resources/Photos/cat4.jpg')
resized_image = rescaleFrame(img, scale=.2)
cv.imshow('Cats', img)
cv.imshow('Cats_resized', resized_image)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('Resources/Videos/cat1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
