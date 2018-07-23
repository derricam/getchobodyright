def startAvatarPage():
    size(1000,800)
    background(147, 103, 89)
    
    textSize(20)
    text("LEFT MOUSE = BODY", 200, 700)
    text("CENTER MOUSE = SHOES ", 200, 725)
    text("RIGHT MOUSE = HAT", 200, 750)
    
    
    
    
    
    #1
    fill(255,255,255)
    rect(0,0,50,50)
    #2
    fill(0,0,0)
    rect(0,50,50,50)
    #3
    fill(255, 0, 0)
    rect(0,100,50,50)
    #4
    fill(0, 255, 0)
    rect(0,150,50,50)
    #5
    fill(0, 0, 255)
    rect(0,200,50,50)
    #6
    fill(255, 255, 0)
    rect(0,250,50,50)
    #7
    fill(0, 255, 255)
    rect(0,300,50,50)
    
    

def drawBody():
        if mousePressed and mouseButton == LEFT:
            if mouseX <= 150 and mouseY <= 400:
                ellipse(350, 50, 50, 75)
        if mousePressed and mouseButton == LEFT:
            if mouseX <= 150 and mouseY <= 400:
                ellipse(350, 200, 125, 200)
        
def mouseFunction():         
        if mouseButton == RIGHT:
            if mouseX <= 50 and mouseY < 50:
                fill(255, 255, 255)
            if mouseX <= 50 and mouseY > 50 and mouseY <=100:
                fill(0, 0, 0)
            if mouseX <= 50 and mouseY > 100 and mouseY <=150:
                fill(255, 0, 0)
            if mouseX <=50 and mouseY > 150 and mouseY <=200:
                fill(0, 255, 0)
            if mouseX <=50 and mouseY > 200 and mouseY <=250:
                fill(0, 0, 255)
            if mouseX <=50 and mouseY > 250 and mouseY <=300:
                fill(255, 255, 0)
            if mouseX <=50 and mouseY > 300 and mouseY <=350:
                fill(0, 255, 255)
        triangle(350, 0, 400, 45, 300, 25)
    
        if mouseButton == CENTER:
            if mouseX <= 50 and mouseY < 50:
                fill(255, 255, 255)
            if mouseX <= 50 and mouseY > 50 and mouseY <=100:
                fill(0, 0, 0)
            if mouseX <= 50 and mouseY > 100 and mouseY <=150:
                fill(255, 0, 0)
            if mouseX <=50 and mouseY > 150 and mouseY <=200:
                fill(0, 255, 0)
            if mouseX <=50 and mouseY > 200 and mouseY <=250:
                fill(0, 0, 255)
            if mouseX <=50 and mouseY > 250 and mouseY <=300:
                fill(255, 255, 0)
            if mouseX <=50 and mouseY > 300 and mouseY <=350:
                fill(0, 255, 255)
        triangle(350, 310, 400, 350, 300, 340)
