import time
import cv2
camera_port = 2
y = 0
x = 0
h = 480
w = 480


camera = cv2.VideoCapture(camera_port)

camera.set(cv2.CAP_PROP_EXPOSURE, -6)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#time.sleep(0.005)  # If you don't wait, the image will be dark

for i in range(0,10):
    time.sleep(i/10)
    return_value, image = camera.read()
    final_image = image[y:y+h, x:x+w]
    #resized_image = cv2.resize(image, (320, 320))
    cv2.imwrite("C:/Users/Harry/AppData/Local/Programs/Python/Python38-32/opencv" + str(i) + ".png", final_image)
    print(i)
 
'''
return_value, image = camera.read()

cv2.imwrite("C:/Users/Harry/AppData/Local/Programs/Python/Python38-32/opencv.png", image)
'''

del(camera)  # so that others can use the camera as soon as possible