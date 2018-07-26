add_library('minim')

xCoord = 550
yCoord = 410
previousX = 550
previousY = 410
power = "on"
musicPlaying = False


stations = {"101.1" : "Hip Hop",
            "107.5" : "Classics",
            "99.7" : "TRAP",
            "100.1" : "JIG"}

textDisplayed = ""
previousText =""

def radioBackground():
<<<<<<< HEAD
    background(0,0,0)
    size(1000,800)
    global player, player1, player2, player3
=======
    #background(122,197,205)
    sky = loadImage("sky6.jpg")
    image(sky, 0, -250, 1000, 584)
    stroke(0)
    strokeWeight(12)
    fill(60, 60, 60)
    bezier(-100, 230, 250, 200, 750, 200, 1100, 230)
    noStroke()
    rect(0, 230, 1000, 570)
    size(1000,800)
    global player, player1, player2, player3, sky
>>>>>>> 557b625ae461c45e9dd63a5f870aed18f058a95a

    #radio
    strokeWeight(4)
    stroke("#868585")
    fill(138,54,15)
    rect(150,250,500,300, 30)

    #speaker
    strokeWeight(7)
    stroke("#4D4D4D")
    fill(255)
    ellipse(260,400,150,150)
    ellipse(260, 400, 100, 100)
    noStroke()
    fill(0)
    ellipse(260, 400, 30, 30)
    
    #steering wheel
    fill(10)
    bezier(690, 460, 710, 390, 890, 395, 990, 460)
    rect(960, 440, 80, 300)
    stroke(156,102,31)
    strokeWeight(50)
    noFill()
    ellipse(990, 450, 600, 600)
    fill(156,102,31)
    noStroke()
    ellipse(990, 450, 300, 250)

    #dial base
    stroke("#4D4D4D")
    fill(0)
    strokeWeight(5)
    ellipse(550,430,60,60)

    #stations
    fill(0)
    textSize(10)
    text("99.7", 490, 433)
    text("100.1", 535, 396)
    text("101.1", 583, 433)
    text("107.5", 535, 474)

    # #display
    stroke("#4D4D4D")
    fill(255)
    rect(395,293,190,60)

    font = loadFont("Ravie-15.vlw")
    textFont(font, 15)
    text("! ! ALWAYS TURN OFF STATION BEFORE YOU START ANOTHER ! !", 100, 630)
    text("LEFT CLICK TO PLAY", 300, 660)
    text("RIGHT CLICK TO STOP", 300, 680)


# def draw():
#      musicStation()

def musicStation(player, player1, player2, player3):
    global xCoord, yCoord, previousX, previousY, stations, textDisplayed, previousText, clicked, musicPlaying, sky

    if mousePressed and mouseButton == LEFT and mouseX >= 483 and mouseX <550 and mouseY > 411 and mouseY <446 and musicPlaying == False: #play trap
        
        previousX = xCoord
        previousY = yCoord
        xCoord = 530
        yCoord = 427
        previousText = textDisplayed
        textDisplayed = stations["99.7"]
        fill(240,230,140)
        rect(400,306,100,40)

        player.play()
        musicPlaying = True

    if mousePressed and mouseButton == RIGHT and mouseX >= 483 and mouseX <550 and mouseY > 411 and mouseY <446 and musicPlaying == True:
        player.close()
        musicPlaying = False

    if mousePressed and mouseButton == LEFT and mouseX >= 530 and mouseX <580 and mouseY > 380 and mouseY <420 and musicPlaying == False: #play R&B
        previousX = xCoord
        previousY = yCoord
        xCoord = 550
        yCoord = 410
        previousText = textDisplayed
        textDisplayed = stations["100.1"]
        fill(240,230,140)
        rect(400,306,100,40)

        player1.play()
        musicPlaying = True
    if mousePressed and mouseButton == RIGHT and mouseX >= 530 and mouseX <580 and mouseY > 380 and mouseY <420 and musicPlaying == True:
        player1.close()
        musicPlaying = False

    if mousePressed and mouseButton == LEFT and mouseX >= 555 and mouseX <612 and mouseY > 413 and mouseY <441 and musicPlaying == False: #play hip hop
        previousX = xCoord
        previousY = yCoord
        xCoord = 571
        yCoord = 428
        previousText = textDisplayed
        textDisplayed = stations["101.1"]
        fill(240,230,140)
        rect(400,306,100,40)

        player2.play()
        musicPlaying = True

    if mousePressed and mouseButton == RIGHT and mouseX >= 555 and mouseX <612 and mouseY > 413 and mouseY <441 and musicPlaying == True:
        player2.close()
        musicPlaying = False

    if mousePressed and mouseButton == LEFT and mouseX >= 526 and mouseX <572 and mouseY > 438 and mouseY <477 and musicPlaying == False: #play classic
        previousX = xCoord
        previousY = yCoord
        xCoord = 550
        yCoord = 451
        previousText = textDisplayed
        textDisplayed = stations["107.5"]
        fill(240,230,140)
        rect(400,306,100,40)

        player3.play()
        musicPlaying = True

    if mousePressed and mouseButton == RIGHT and mouseX >= 526 and mouseX <572 and mouseY > 438 and mouseY <477 and musicPlaying == True:
        player3.close()
        musicPlaying = False

    noStroke()
    fill(240,230,140)
    text(previousText,402,326)
    fill("#4D4D4D")
    text(textDisplayed,402,326)

    noStroke()
    fill("#717171")
    ellipse(previousX,previousY, 10,10)
    fill("#4D4D4D")
    ellipse(xCoord,yCoord, 10,10)

def musicPlayed():
    global power, previousX, previousY, xCoord, yCoord, stations, textDisplayed, previousText
    if mouseX > 175 and mouseX < 225 and mouseY >235 and mouseY < 250:
        if power == "off":
            stroke("#4D4D4D")
            fill(240,230,140)
            rect(395,293,190,60)
            fill(0)
            textDisplayed = stations["100.1"]
            previousText = textDisplayed
            power = "on"
        else:
            fill(0)
            stroke("#4D4D4D")
            rect(395,293,190,60)
            textDisplayed = " "
            previousText = " "
            power = "on"
