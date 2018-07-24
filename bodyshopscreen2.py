def makeBackground():
    size(1000, 800)
    global insideOfGarage, bodyR, bodyG, bodyB
    insideOfGarage = loadImage("insideOfGarage.jpg")
    bodyR = 255
    bodyG = 255
    bodyB = 255

def drawCar():
    global insideOfGarage, bodyR, bodyG, bodyB
    image(insideOfGarage, 0, 0, 1000, 800)
    
    #color choices
    stroke(0)
    strokeWeight(1)
    fill(255, 0, 0)
    rect(320, 50, 75, 75, 30)
    fill(0, 0, 255)
    rect(420, 50, 75, 75, 30)
    fill(255, 255, 255)
    rect(520, 50, 75, 75, 30)
    fill(0, 0, 0)
    rect(620, 50, 75, 75, 30)
    
    #color light when hover
    if (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(255, 0, 0)
        rect(320, 50, 75, 75, 30)
    elif (mouseX >= 420 and mouseX <= 495) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 0, 255)
        rect(420, 50, 75, 75, 30)
    elif (mouseX >= 520 and mouseX <= 595) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 520, 0)
        strokeWeight(4)
        fill(255, 255, 255)
        rect(520, 50, 75, 75, 30)
    elif (mouseX >= 620 and mouseX <= 695) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 0, 0)
        rect(620, 50, 75, 75, 30)
    
    #body of car
    noStroke()
    fill(bodyR, bodyG, bodyB)
    bezier(200, 450, 500, 300, 650, 250, 800, 450) #top of the body
    rect(110, 440, 780, 130, 10, 2000, 200, 20) #bottom of body
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    bezier(230, 440, 500, 310, 650, 260, 780, 440) #windows
    fill(0)
    rect(350, 378, 2, 192)
    rect(560, 318, 2, 252)
    rect(793, 440, 2, 130)
    noFill()
    stroke(60)
    strokeWeight(2)
    ellipse(385, 460, 30, 10) #door handles
    ellipse(595, 460, 30, 10)
    
    #lights
    fill(255,215,0)
    ellipse(860, 490, 20, 40)
    fill(255,64,64)
    ellipse(130, 490, 20, 40)
    
    #tires
    stroke(60)
    fill(0)
    ellipse(220, 570, 100, 100)
    ellipse(780, 570, 100, 100)
    ellipse(220, 570, 90, 90)
    ellipse(780, 570, 90, 90)
    
    fill(255,215,0)
    textSize(35)
    text("Pick a Body Color!", 300, 700)
    
def drawTruck():
    pass
    # def drawCar():
    # global insideOfGarage, bodyR, bodyG, bodyB
    # image(insideOfGarage, 0, 0, 1000, 800)
    
    # #color choices
    # stroke(0)
    # strokeWeight(1)
    # fill(255, 0, 0)
    # rect(320, 50, 75, 75, 30)
    # fill(0, 0, 255)
    # rect(420, 50, 75, 75, 30)
    # fill(255, 255, 255)
    # rect(520, 50, 75, 75, 30)
    # fill(0, 0, 0)
    # rect(620, 50, 75, 75, 30)
    
    # #color light when hover
    # if (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
    #     stroke(0, 255, 0)
    #     strokeWeight(4)
    #     fill(255, 0, 0)
    #     rect(320, 50, 75, 75, 30)
    # elif (mouseX >= 420 and mouseX <= 495) and (mouseY >= 50 and mouseY <= 125):
    #     stroke(0, 255, 0)
    #     strokeWeight(4)
    #     fill(0, 0, 255)
    #     rect(420, 50, 75, 75, 30)
    # elif (mouseX >= 520 and mouseX <= 595) and (mouseY >= 50 and mouseY <= 125):
    #     stroke(0, 520, 0)
    #     strokeWeight(4)
    #     fill(255, 255, 255)
    #     rect(520, 50, 75, 75, 30)
    # elif (mouseX >= 620 and mouseX <= 695) and (mouseY >= 50 and mouseY <= 125):
    #     stroke(0, 255, 0)
    #     strokeWeight(4)
    #     fill(0, 0, 0)
    #     rect(620, 50, 75, 75, 30)
    
    # #body of car
    # noStroke()
    # fill(bodyR, bodyG, bodyB)
    # bezier(200, 450, 500, 300, 650, 250, 800, 450) #top of the body
    # rect(110, 440, 780, 130, 10, 2000, 200, 20) #bottom of body
    
    # #doors and windows
    # windowR = 60
    # windowG = 60
    # windowB = 60
    # fill(windowR, windowG, windowB)
    # bezier(230, 440, 500, 310, 650, 260, 780, 440) #windows
    # fill(0)
    # rect(350, 378, 2, 192)
    # rect(560, 318, 2, 252)
    # rect(793, 440, 2, 130)
    # noFill()
    # stroke(60)
    # strokeWeight(2)
    # ellipse(385, 460, 30, 10) #door handles
    # ellipse(595, 460, 30, 10)
    
    # #lights
    # fill(255,215,0)
    # ellipse(860, 490, 20, 40)
    # fill(255,64,64)
    # ellipse(130, 490, 20, 40)
    
    # #tires
    # stroke(60)
    # fill(0)
    # ellipse(220, 570, 100, 100)
    # ellipse(780, 570, 100, 100)
    # ellipse(220, 570, 90, 90)
    # ellipse(780, 570, 90, 90)
    
    # fill(255,215,0)
    # textSize(35)
    # text("Pick a Body Color!", 300, 700)
    
def drawBus():
    pass
    # def drawCar():
    # global insideOfGarage, bodyR, bodyG, bodyB
    # image(insideOfGarage, 0, 0, 1000, 800)
    
    # #color choices
    # stroke(0)
    # strokeWeight(1)
    # fill(255, 0, 0)
    # rect(320, 50, 75, 75, 30)
    # fill(0, 0, 255)
    # rect(420, 50, 75, 75, 30)
    # fill(255, 255, 255)
    # rect(520, 50, 75, 75, 30)
    # fill(0, 0, 0)
    # rect(620, 50, 75, 75, 30)
    
    # #color light when hover
    # if (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
    #     stroke(0, 255, 0)
    #     strokeWeight(4)
    #     fill(255, 0, 0)
    #     rect(320, 50, 75, 75, 30)
    # elif (mouseX >= 420 and mouseX <= 495) and (mouseY >= 50 and mouseY <= 125):
    #     stroke(0, 255, 0)
    #     strokeWeight(4)
    #     fill(0, 0, 255)
    #     rect(420, 50, 75, 75, 30)
    # elif (mouseX >= 520 and mouseX <= 595) and (mouseY >= 50 and mouseY <= 125):
    #     stroke(0, 520, 0)
    #     strokeWeight(4)
    #     fill(255, 255, 255)
    #     rect(520, 50, 75, 75, 30)
    # elif (mouseX >= 620 and mouseX <= 695) and (mouseY >= 50 and mouseY <= 125):
    #     stroke(0, 255, 0)
    #     strokeWeight(4)
    #     fill(0, 0, 0)
    #     rect(620, 50, 75, 75, 30)
    
    # #body of car
    # noStroke()
    # fill(bodyR, bodyG, bodyB)
    # bezier(200, 450, 500, 300, 650, 250, 800, 450) #top of the body
    # rect(110, 440, 780, 130, 10, 2000, 200, 20) #bottom of body
    
    # #doors and windows
    # windowR = 60
    # windowG = 60
    # windowB = 60
    # fill(windowR, windowG, windowB)
    # bezier(230, 440, 500, 310, 650, 260, 780, 440) #windows
    # fill(0)
    # rect(350, 378, 2, 192)
    # rect(560, 318, 2, 252)
    # rect(793, 440, 2, 130)
    # noFill()
    # stroke(60)
    # strokeWeight(2)
    # ellipse(385, 460, 30, 10) #door handles
    # ellipse(595, 460, 30, 10)
    
    # #lights
    # fill(255,215,0)
    # ellipse(860, 490, 20, 40)
    # fill(255,64,64)
    # ellipse(130, 490, 20, 40)
    
    # #tires
    # stroke(60)
    # fill(0)
    # ellipse(220, 570, 100, 100)
    # ellipse(780, 570, 100, 100)
    # ellipse(220, 570, 90, 90)
    # ellipse(780, 570, 90, 90)
    
    # fill(255,215,0)
    # textSize(35)
    # text("Pick a Body Color!", 300, 700)
    
def pickColor():
    global bodyR, bodyG, bodyB
    if (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 255
        bodyG = 0
        bodyB = 0
    if (mouseX >= 420 and mouseX <= 495) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 0
        bodyG = 0
        bodyB = 255
    if (mouseX >= 520 and mouseX <= 595) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 255
        bodyG = 255
        bodyB = 255
    if (mouseX >= 620 and mouseX <= 695) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 0
        bodyG = 0
        bodyB = 0
        
