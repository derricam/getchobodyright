from functionsList import *
from bodyshop_background import *
from bodyshopscreen2 import *
from spongebob import *


def setup():
    size(1000, 800)
    global screen
    
    screen = "one"
    vehicle = "car"
    
    if screen == "one":
        backgroundImage()
    

def draw():
    global screen, vehicle
    
    if screen == "one":
        backgroundTextAndBoxes()
    elif screen == "two" and vehicle == "car":
        drawCar()
    elif screen == "two" and vehicle == "truck":
        drawTruck()
    elif screen == "two" and vehicle == "bus":
        drawBus()
    elif screen == "three":
        #drawBody()
        spongebob()
        
        
def mouseClicked():
    global vehicle
    global screen
    if screen == "two":
        pickColor()
    if screen == "three":
        mouseFunction()
        
    if screen == "one" and (mouseX >= 50 and mouseX <= 200) and (mouseY >= 325 and mouseY <= 475):
        screen = "two"
        vehicle = "car"
        makeBackground()
    if screen == "one" and (mouseX >= 425 and mouseX <= 600) and (mouseY >= 325 and mouseY <= 475):
        screen = "two"
        vehicle = "truck"
        makeBackground()
    if screen == "one" and (mouseX >= 800 and mouseX <= 950) and (mouseY >= 325 and mouseY <= 475):
        screen = "two"
        vehicle = "bus"
        makeBackground()
    if screen == "two" and (mouseX >= 880 and mouseX <= 980) and (mouseY >= 700 and mouseY <= 780):
        screen = "three"
        startAvatarPage()
