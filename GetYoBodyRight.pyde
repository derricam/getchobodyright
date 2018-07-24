from functionsList import *
#from functionsList import *
from bodyshop_background import *
from bodyshopscreen2 import *
def setup():
    size(1000, 800)
    global me
    
    screen = "one"
    
    if screen == "one":
        backgroundImage()
    

def draw():
    global screen
    
    if screen == "one":
        backgroundTextAndBoxes()
    elif screen == "two":
        drawCar()
    # else:
    #     startAvatarPage()
    #     drawBody()
        
        
def mouseClicked():
    global screen
    pickColor()
    if screen == "one" and (mouseX >= 50 and mouseX <= 200) and (mouseY >= 325 and mouseY <= 475):
        screen = "two"
        makeBackground()
