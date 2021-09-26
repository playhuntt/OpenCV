import cv2 as cv

# Reading Image
img = cv.imread('Photos/cat4.jpg')
cv.imshow('Cats', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('Videos/cat1.mp4')

while True:
    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
