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
