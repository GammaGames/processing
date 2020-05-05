
def setup():
    pass

    
def draw():    
    pass
    
    
def keyPressed():
    k = str(key)
    if k == " ":
        redraw()
    elif k == "s":
        saveFrame("output.png")
