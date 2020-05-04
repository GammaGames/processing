import random

def setup():
    global img
    random.seed()
    
    img = loadImage("../img/blossom_chriswearly.jpeg")
    img.loadPixels()
    img.resize(int(img.width / 2), int(img.height / 2))
    this.getSurface().setSize(img.width, img.height)
    
    colorMode(HSB, 360, 100, 100)
    strokeWeight(5)
    strokeCap(ROUND)
    noLoop()

    
def draw():    
    # image(img, 0, 0, width, height)
    background(0, 0, 0)
    
    x_offset = img.width * -1
    while x_offset < width:
        cur_x_offset = x_offset
        y_offset = 0
        while y_offset < height:
            if y_offset * img.width + cur_x_offset > len(img.pixels):
                break
            col = img.pixels[y_offset * img.width + cur_x_offset]
            stroke(col)
            length = random.randint(15, 60)
            line(cur_x_offset, y_offset, cur_x_offset + length / 2, y_offset + length)
            y_offset += length + 10
            cur_x_offset += length / 2 + 5
        x_offset += 12
    saveFrame("output.png")
