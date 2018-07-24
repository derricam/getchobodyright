from functionsList import *
<<<<<<< HEAD
from bodyshop_background import *
from spongebob import *
=======
#from functionsList import *
from bodyshop_background import *
from bodyshopscreen2 import *
>>>>>>> d7f46f593ac43ddfed62fc6b7a930b4a3b0702b3
def setup():
    size(1000, 800)
    global screen
    
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
<<<<<<< HEAD
    mouseFunction()
    spongebob()
=======
    global screen
    pickColor()
    if screen == "one" and (mouseX >= 50 and mouseX <= 200) and (mouseY >= 325 and mouseY <= 475):
        screen = "two"
        makeBackground()
>>>>>>> d7f46f593ac43ddfed62fc6b7a930b4a3b0702b3
