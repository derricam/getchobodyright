def backgroundImage():
    global garageBackground
    size(1000,800)
    garageBackground = loadImage("garageBackground.jpeg")

def backgroundTextAndBoxes():
    #garageBackground = loadImage("garageBackground.jpeg")
    image(garageBackground, 0, 0, 1000, 800)
    font = loadFont("Ravie-58.vlw")
    fill(255)
    textFont(font,58)
    fill(255)
    text("Get'cho Body Right",150,150)
    stroke(0)
    rect(50,325,150,150,30)
    rect(425,325,150,150,30)
    rect(800,325,150,150,30)
    strokeWeight(4)
    
    if (mouseX >= 50 and mouseX <= 200) and (mouseY >= 325 and mouseY <= 475):
        stroke(204, 102, 0)
        rect(50,325,150,150,30)
    if (mouseX >= 425 and mouseX <= 600) and (mouseY >= 325 and mouseY <= 475):
        stroke(204, 102, 0)
        rect(425,325,150,150,30)
    if (mouseX >= 800 and mouseX <= 950) and (mouseY >= 325 and mouseY <= 475):
        stroke(204, 102, 0)
        rect(800,325,150,150,30)
