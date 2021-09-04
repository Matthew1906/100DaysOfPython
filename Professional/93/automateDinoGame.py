from PIL import ImageGrab, ImageOps
from pyautogui import press, moveTo
from time import sleep
from numpy import array
  
dinosaur_coordinates = (215, 600)
 
def imageGrab():
    image = array(ImageOps.grayscale(ImageGrab.grab()))
    for i in range(dinosaur_coordinates[1]-50, dinosaur_coordinates[1]+110):
        for j in range(dinosaur_coordinates[0]+35, dinosaur_coordinates[0]+120):
            if image[i,j] != 255:
                return True
    
# Start Game
sleep(5)
press('up')

# Jump
while True:
    if imageGrab():
        press('up')      