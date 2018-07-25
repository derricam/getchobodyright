def makeBackground():
    size(1000, 800)
    global insideOfGarage, bodyR, bodyG, bodyB, tireR, tireG, tireB
    insideOfGarage = loadImage("insideOfGarage.jpg")
    bodyR = 255
    bodyG = 255
    bodyB = 255
    tireR = 0
    tireG = 0
    tireB = 0

def drawCar():
    global insideOfGarage, bodyR, bodyG, bodyB, tireR, tireG, tireB
    image(insideOfGarage, 0, 0, 1000, 800)
    
    #color choices
    stroke(0)
    strokeWeight(1)
    fill(238,180,34)
    rect(120, 50, 75, 75, 30)
    fill(238,18,137)
    rect(220, 50, 75, 75, 30)
    fill(255, 0, 0)
    rect(320, 50, 75, 75, 30)
    fill(0, 0, 255)
    rect(420, 50, 75, 75, 30)
    fill(255, 255, 255)
    rect(520, 50, 75, 75, 30)
    fill(0, 0, 0)
    rect(620, 50, 75, 75, 30)
    fill(104,34,139)
    rect(720, 50, 75, 75, 30)
    fill(0,128,0)
    rect(820, 50, 75, 75, 30)
    
    
    # #tire color options
    # fill(60, 60, 60)
    # rect(25, 650, 75, 30, 30)
    
    #color light when hover
    if (mouseX >= 120 and mouseX <= 195) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 180, 34)
        rect(120, 50, 75, 75, 30)
    elif (mouseX >= 220 and mouseX <= 295) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 18, 137)
        rect(220, 50, 75, 75, 30)
    elif (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
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
    elif (mouseX >= 720 and mouseX <= 795) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(104, 34, 139)
        rect(720, 50, 75, 75, 30)
    elif (mouseX >= 820 and mouseX <= 895) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 128, 0)
        rect(820, 50, 75, 75, 30)
    
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
    ellipse(220, 570, 80, 80)
    ellipse(780, 570, 80, 80)
    
    fill(255,215,0)
    textSize(35)
    text("Pick a Body Color!", 300, 700)
    
    #next button
    fill(0, 255, 0)
    rect(880, 700, 100, 80, 30)
    fill(255)
    textSize(25)
    text("NEXT", 888, 750)
    if (mouseX >= 880 and mouseX <= 980) and (mouseY >= 700 and mouseY <= 780):
        fill(0, 255, 0)
        stroke(127,255,0)
        rect(880, 700, 100, 80, 30)
        fill(255)
        textSize(25)
        text("NEXT", 888, 750)
        
    #back button
    stroke(0)
    strokeWeight(1)
    fill(255, 0, 0)
    rect(20, 700, 100, 80, 30)
    fill(0)
    textSize(25)
    text("BACK", 28, 750)
    if (mouseX >= 20 and mouseX <= 120) and (mouseY >= 700 and mouseY <= 780):
        fill(255, 0, 0)
        stroke(255,0,0)
        rect(20, 700, 100, 80, 30)
        fill(0)
        textSize(25)
        text("BACK", 28, 750)
    
def drawTruck():
    pass
    global insideOfGarage, bodyR, bodyG, bodyB, tireR, tireG, tireB
    image(insideOfGarage, 0, 0, 1000, 800)
    
    #color choices
    stroke(0)
    strokeWeight(1)
    fill(238,180,34)
    rect(120, 50, 75, 75, 30)
    fill(238,18,137)
    rect(220, 50, 75, 75, 30)
    fill(255, 0, 0)
    rect(320, 50, 75, 75, 30)
    fill(0, 0, 255)
    rect(420, 50, 75, 75, 30)
    fill(255, 255, 255)
    rect(520, 50, 75, 75, 30)
    fill(0, 0, 0)
    rect(620, 50, 75, 75, 30)
    fill(104,34,139)
    rect(720, 50, 75, 75, 30)
    fill(0,128,0)
    rect(820, 50, 75, 75, 30)
    
    #color light when hover
    if (mouseX >= 120 and mouseX <= 195) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 180, 34)
        rect(120, 50, 75, 75, 30)
    elif (mouseX >= 220 and mouseX <= 295) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 18, 137)
        rect(220, 50, 75, 75, 30)
    elif (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
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
    elif (mouseX >= 720 and mouseX <= 795) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(104, 34, 139)
        rect(720, 50, 75, 75, 30)
    elif (mouseX >= 820 and mouseX <= 895) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 128, 0)
        rect(820, 50, 75, 75, 30)
    
    #body of truck
    noStroke()
    fill(bodyR, bodyG, bodyB)
    rect(110, 380, 780, 190, 10, 20, 20, 20) #bottom of body
    quad(360, 380, 390, 210, 660, 210, 720, 380)
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    quad(370, 380, 400, 230, 650, 230, 705, 380)
    fill(0)
    rect(490, 225, 2, 345)
    rect(490, 225, 165, 2)
    rect(708, 375, 2, 195)
    quad(655, 225, 657, 225, 710, 375, 708, 375)
    noFill()
    stroke(60)
    strokeWeight(2)
    ellipse(515, 410, 30, 10) #door handles
    
    #lights
    fill(255,215,0)
    ellipse(860, 430, 20, 40)
    fill(255,64,64)
    ellipse(130, 430, 20, 40)
    
    #tires
    stroke(60)
    fill(0)
    ellipse(220, 570, 100, 100)
    ellipse(780, 570, 100, 100)
    ellipse(220, 570, 80, 80)
    ellipse(780, 570, 80, 80)
    
    fill(255,215,0)
    textSize(35)
    text("Pick a Body Color!", 300, 700)
    
    #next button
    fill(0, 255, 0)
    rect(880, 700, 100, 80, 30)
    fill(255)
    textSize(25)
    text("NEXT", 888, 750)
    if (mouseX >= 880 and mouseX <= 980) and (mouseY >= 700 and mouseY <= 780):
        fill(0, 255, 0)
        stroke(127,255,0)
        rect(880, 700, 100, 80, 30)
        fill(255)
        textSize(25)
        text("NEXT", 888, 750)
        
    #back button
    stroke(0)
    strokeWeight(1)
    fill(255, 0, 0)
    rect(20, 700, 100, 80, 30)
    fill(0)
    textSize(25)
    text("BACK", 28, 750)
    if (mouseX >= 20 and mouseX <= 120) and (mouseY >= 700 and mouseY <= 780):
        fill(255, 0, 0)
        stroke(255,0,0)
        rect(20, 700, 100, 80, 30)
        fill(0)
        textSize(25)
        text("BACK", 28, 750)
    
def drawBus():
    global insideOfGarage, bodyR, bodyG, bodyB, tireR, tireG, tireB
    image(insideOfGarage, 0, 0, 1000, 800)
    
    #color choices
    stroke(0)
    strokeWeight(1)
    fill(238,180,34)
    rect(120, 50, 75, 75, 30)
    fill(238,18,137)
    rect(220, 50, 75, 75, 30)
    fill(255, 0, 0)
    rect(320, 50, 75, 75, 30)
    fill(0, 0, 255)
    rect(420, 50, 75, 75, 30)
    fill(255, 255, 255)
    rect(520, 50, 75, 75, 30)
    fill(0, 0, 0)
    rect(620, 50, 75, 75, 30)
    fill(104,34,139)
    rect(720, 50, 75, 75, 30)
    fill(0,128,0)
    rect(820, 50, 75, 75, 30)
    
    #color light when hover
    if (mouseX >= 120 and mouseX <= 195) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 180, 34)
        rect(120, 50, 75, 75, 30)
    elif (mouseX >= 220 and mouseX <= 295) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(238, 18, 137)
        rect(220, 50, 75, 75, 30)
    elif (mouseX >= 320 and mouseX <= 395) and (mouseY >= 50 and mouseY <= 125):
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
    elif (mouseX >= 720 and mouseX <= 795) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(104, 34, 139)
        rect(720, 50, 75, 75, 30)
    elif (mouseX >= 820 and mouseX <= 895) and (mouseY >= 50 and mouseY <= 125):
        stroke(0, 255, 0)
        strokeWeight(4)
        fill(0, 128, 0)
        rect(820, 50, 75, 75, 30)
    
    #body of bus
    noStroke()
    fill(bodyR, bodyG, bodyB)
    rect(110, 220, 680, 350, 30, 30, 0, 10) #top of body
    rect(790, 380, 100, 190, 0, 50, 10, 0) #hood
    fill(60)
    text("MAGIC SCHOOL BUS", 300, 465)
    
    #doors and windows
    windowR = 60
    windowG = 60
    windowB = 60
    fill(windowR, windowG, windowB)
    rect(125, 235, 120, 150, 30)
    rect(260, 235, 120, 150, 30)
    rect(395, 235, 120, 150, 30)
    rect(530, 235, 120, 150, 30)
    rect(665, 235, 110, 150, 30)
    rect(140, 400, 600, 10)
    rect(140, 490, 600, 10)
    
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
    
    #tires
    stroke(60)
    fill(0)
    ellipse(220, 570, 120, 120)
    ellipse(780, 570, 120, 120)
    ellipse(220, 570, 100, 100)
    ellipse(780, 570, 100, 100)
    
    fill(255,215,0)
    textSize(35)
    text("Pick a Body Color!", 300, 700)
    
    #next button
    fill(0, 255, 0)
    rect(880, 700, 100, 80, 30)
    fill(255)
    textSize(25)
    text("NEXT", 888, 750)
    if (mouseX >= 880 and mouseX <= 980) and (mouseY >= 700 and mouseY <= 780):
        fill(0, 255, 0)
        stroke(127,255,0)
        rect(880, 700, 100, 80, 30)
        fill(255)
        textSize(25)
        text("NEXT", 888, 750)
    
    #back button
    stroke(0)
    strokeWeight(1)
    fill(255, 0, 0)
    rect(20, 700, 100, 80, 30)
    fill(0)
    textSize(25)
    text("BACK", 28, 750)
    if (mouseX >= 20 and mouseX <= 120) and (mouseY >= 700 and mouseY <= 780):
        fill(255, 0, 0)
        stroke(255,0,0)
        rect(20, 700, 100, 80, 30)
        fill(0)
        textSize(25)
        text("BACK", 28, 750)
    
def pickColor():
    global bodyR, bodyG, bodyB, tireR, tireG, tireB
    if (mouseX >= 120 and mouseX <= 195) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 238
        bodyG = 180
        bodyB = 34
    if (mouseX >= 220 and mouseX <= 295) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 238
        bodyG = 18
        bodyB = 137
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
    if (mouseX >= 720 and mouseX <= 795) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 104
        bodyG = 34
        bodyB = 139
    if (mouseX >= 820 and mouseX <= 895) and (mouseY >= 50 and mouseY <= 125):
        bodyR = 0
        bodyG = 128
        bodyB = 0
