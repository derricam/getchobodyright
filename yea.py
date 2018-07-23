add_library('sound')


def setup():
    global file
    size(600, 400)
    background(255)
    
  # Load a soundfile from the /data folder of the sketch and play it back
    file = SoundFile("Profound Beats - Lo-Fi.mp3")

     

def draw():
    pass
    
def mouseClicked():
    # Play sound when mouse clicked on canvas.
    file.play()
    
    
    triangle(350, 315, 370, 350, 310, 340)
