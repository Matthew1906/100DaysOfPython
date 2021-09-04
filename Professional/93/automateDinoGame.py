from PIL import ImageGrab, ImageOps
from pyautogui import press, moveTo
from time import sleep
from numpy import array
  
dinosaur_coordinates = (210, 600)
 
def imageGrab():
    box = (dinosaur_coordinates[0]+40, dinosaur_coordinates[1]-50, dinosaur_coordinates[0]+130, dinosaur_coordinates[1]+150)
    # moveTo(dinosaur_coordinates[0]+10, dinosaur_coordinates[1]-50)
    # sleep(2.5)  
    # moveTo(dinosaur_coordinates[0]+10, dinosaur_coordinates[1]+100)
    # sleep(2.5)
    # moveTo(dinosaur_coordinates[0]+100, dinosaur_coordinates[1]-50)
    # sleep(2.5)
    # moveTo(dinosaur_coordinates[0]+100, dinosaur_coordinates[1]+100)
    # sleep(2.5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a)
    print(a.sum())
    return a.sum()
    
sleep(5)
# moveTo(dinosaur_coordinates)
while True:
    if imageGrab() not in [18038, 18338]:
        print('jump')
        press('up')      