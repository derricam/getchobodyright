def startAvatarPage():
    size(1000,800)
    background(147, 103, 89)
    
    textSize(20)
    text("LEFT MOUSE = BODY", 200, 700)
    text("CENTER MOUSE = ", 200, 725)
    text("LEFT MOUSE = BODY", 200, 750)
    
    
    
    
    
    
    fill(255,255,255)
    rect(0,0,50,50)
    
    fill(0,0,0)
    rect(0,50,50,50)
    
    fill(247, 2, 39)
    rect(0,100,50,50)
    
    fill(216, 2, 138)
    rect(0,150,50,50)
    
    fill(144, 2, 216)
    rect(0,200,50,50)
    
    fill(150, 60, 216)
    rect(0,250,50,50)
    
    fill(100, 216, 215)
    rect(0,300,50,50)
    
    fill(2, 216, 111)
    rect(50,0,50,50)
    
    fill(37, 216, 2)
    rect(50,50,50,50)
    
    fill(247, 247, 5)
    rect(50,100,50,50)
    
    fill(204, 205, 30)
    rect(50,150,50,50)
    
    fill(252, 188, 60)
    rect(50,200,50,50)
    
    fill(250, 133, 8)
    rect(50,250,50,50)
    
    fill(90, 77, 72)
    rect(50,300,50,50)

def drawBody():
        if mousePressed and mouseButton == LEFT:
            if mouseX <= 150 and mouseY <= 400:
                print("1st")
        if mousePressed and mouseButton == LEFT:
            if mouseX <= 150 and mouseY <= 400:
                print("2nd")
        
def mouseFunction():
    
        if mouseButton == LEFT:

            if mouseX <= 50 and mouseY < 50:
                fill(255, 255, 255)
            if mouseX <= 50 and mouseY > 50 and mouseY <=100:
                fill(0, 0, 0)
            if mouseX <= 50 and mouseY > 100 and mouseY <=150:
                fill(247, 2, 39)
            if mouseX <=50 and mouseY > 150 and mouseY <=200:
                fill(216, 2, 138)
            if mouseX <=50 and mouseY > 200 and mouseY <=250:
                fill(144, 2, 216)
            if mouseX <=50 and mouseY > 250 and mouseY <=300:
                fill(150, 60, 216)
            if mouseX <=50 and mouseY > 300 and mouseY <=350:
                fill(100, 216, 215)
            if mouseX > 50 and mouseY < 100 and mouseY <=50:
                fill(2, 216, 111)
            if mouseX > 50 and mouseY < 150 and mouseY <=100:
                fill(37, 216, 2)
            if mouseX > 50 and mouseY < 200 and mouseY <=150:
                fill(247, 247, 5)
            if mouseX > 50 and mouseY < 250 and mouseY <=200:
                fill(204, 205, 30)
            if mouseX > 50 and mouseY < 300 and mouseY <=250:
                fill(252, 188, 60)
            if mouseX > 50 and mouseY < 350 and mouseY <=300:
                fill(250, 133, 8)
            if mouseX > 50 and mouseY < 400 and mouseY <=350:
                fill(90, 77, 72)
        ellipse(350, 50, 50, 75)
        ellipse(350, 200, 125, 200) 
        if mouseButton == RIGHT:
            if mouseX <= 50 and mouseY < 50:
                fill(255, 255, 255)
            if mouseX <= 50 and mouseY > 50 and mouseY <=100:
                fill(0, 0, 0)
            if mouseX <= 50 and mouseY > 100 and mouseY <=150:
                fill(247, 2, 39)
            if mouseX <=50 and mouseY > 150 and mouseY <=200:
                fill(216, 2, 138)
            if mouseX <=50 and mouseY > 200 and mouseY <=250:
                fill(144, 2, 216)
            if mouseX <=50 and mouseY > 250 and mouseY <=300:
                fill(150, 60, 216)
            if mouseX <=50 and mouseY > 300 and mouseY <=350:
                fill(100, 216, 215)
            if mouseX > 50 and mouseY < 100 and mouseY <=50:
                fill(2, 216, 111)
            if mouseX > 50 and mouseY < 150 and mouseY <=100:
                fill(37, 216, 2)
            if mouseX > 50 and mouseY < 200 and mouseY <=150:
                fill(247, 247, 5)
            if mouseX > 50 and mouseY < 250 and mouseY <=200:
                fill(204, 205, 30)
            if mouseX > 50 and mouseY < 300 and mouseY <=250:
                fill(252, 188, 60)
            if mouseX > 50 and mouseY < 350 and mouseY <=300:
                fill(250, 133, 8)
            if mouseX > 50 and mouseY < 400 and mouseY <=350:
                fill(90, 77, 72)
        triangle(350, 0, 400, 45, 300, 25)
    
        if mouseButton == CENTER:
        noStroke()
        if mouseX <= 50 and mouseY < 50:
            fill(255, 255, 255)
        if mouseX <= 50 and mouseY > 50 and mouseY <=100:
            fill(0, 0, 0)
        if mouseX <= 50 and mouseY > 100 and mouseY <=150:
            fill(247, 2, 39)
        if mouseX <=50 and mouseY > 150 and mouseY <=200:
            fill(216, 2, 138)
        if mouseX <=50 and mouseY > 200 and mouseY <=250:
            fill(144, 2, 216)
        if mouseX <=50 and mouseY > 250 and mouseY <=300:
            fill(150, 60, 216)
        if mouseX <=50 and mouseY > 300 and mouseY <=350:
            fill(100, 216, 215)
        if mouseX > 50 and mouseY < 100 and mouseY <=50:
            fill(2, 216, 111)
        if mouseX > 50 and mouseY < 150 and mouseY <=100:
            fill(37, 216, 2)
        if mouseX > 50 and mouseY < 200 and mouseY <=150:
            fill(247, 247, 5)
        if mouseX > 50 and mouseY < 250 and mouseY <=200:
            fill(204, 205, 30)
        if mouseX > 50 and mouseY < 300 and mouseY <=250:
            fill(252, 188, 60)
        if mouseX > 50 and mouseY < 350 and mouseY <=300:
            fill(250, 133, 8)
        if mouseX > 50 and mouseY < 400 and mouseY <=350:
            fill(90, 77, 72)
        triangle(350, 310, 400, 350, 300, 340)
