<<<<<<< HEAD
from functionsList import *
from bodyshop_background import *
from bodyshopscreen2 import *
def setup():
    size(1000,800)
    startAvatarPage()
    backgroundImage()
    
def draw():
    drawBody()
    backgroundTextAndBoxes()
    
def mouseClicked():
    mouseFunction()
=======
#from functionsList import *
from bodyshop_background import *
from bodyshopscreen2 import *
def setup():
    size(1000, 800)
    global me
    
    me = "mean"
    
    
    if me == "mean":
        makeBackground()
    # else:
    #     startAvatarPage()
    

def draw():
    global me
    if me == "mean":
        drawCar()
#     else:
#         drawBody()
# def mouseClicked():
#     pickColor()
#     mouseFunction()
>>>>>>> 5791fcac58ce3ca62ee51bda01df2d61c16a8dac
