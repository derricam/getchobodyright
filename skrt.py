from bodyshopscreen2 import *

def setupCarDrive():
    size(1000, 800)
    global bodyR, bodyG, bodyB, freeway, carX, carY
    carX = 0
    carY = 440
    # bodyR = 255   #DELETE x3
    # bodyG = 0
    # bodyB = 0
    freeway = loadImage("freeway.png")
    
def driveCar():
    #body of car
    global freeway, carX, carY, bodyR, bodyG, bodyB
    image(freeway, 0, 0, 1150, 874)
    noStroke()
    fill(bodyR, bodyG, bodyB)
    bezier(carX+90, carY+10, carX+390, carY-140, carX+540, carY-190, carX+690, carY+10) #top of the body
    rect(carX, carY, 780, 130, 10, 2000, 200, 20) #bottom of body
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    bezier(carX+120, carY, carX+390, carY-130, carX+540, carY-180, carX+670, carY) #windows
    fill(0)
    rect(carX+240, carY-62, 2, 192)
    rect(carX+450, carY-122, 2, 252)
    rect(carX+683, carY, 2, 130)
    noFill()
    stroke(60)
    strokeWeight(2)
    ellipse(carX+275, carY+20, 30, 10) #door handles
    ellipse(carX+485, carY+20, 30, 10)
    
    #lights
    fill(255,215,0)
    ellipse(carX+750, carY+50, 20, 40)
    fill(255,64,64)
    ellipse(carX+20, carY+50, 20, 40)
    
    #tires
    stroke(60)
    fill(0)
    ellipse(carX+110, carY+130, 100, 100)
    ellipse(carX+670, carY+130, 100, 100)
    ellipse(carX+110, carY+130, 80, 80)
    ellipse(carX+670, carY+130, 80, 80)
    
    carX += 12
    
def driveTruck():
    pass

def drivebus():
    pass
