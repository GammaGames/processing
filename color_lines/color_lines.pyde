import random

col_red = (0, 81, 85)
col_orange = (24, 89, 95)
col_yellow = (45, 97, 98)
col_olive = (68, 88, 80)
col_green = (134, 82, 73)
col_teal = (177, 100, 71)
col_blue = (206, 84, 82)
col_violet = (259, 74, 79)
col_purple = (285, 75, 78)
col_pink = (326, 74, 88)
colors_array = [
    col_red,
    col_orange,
    col_yellow,
    col_olive,
    col_green,
    col_teal,
    col_blue,
    col_violet,
    col_purple,
    col_pink    
]
fib = [1, 1, 2, 3, 5, 8, 13, 21, 34]

def setup():
    global img
    random.seed()
    
    img = loadImage("../img/gamma.png")
    target_size = int(height * 0.8)
    img.resize(target_size, target_size)
    img.loadPixels()
    
    colorMode(HSB, 360, 100, 100)
    strokeWeight(5)
    strokeCap(ROUND)
    noLoop()
    
    size(1000, 500)
    
    
def find_length(x, y, length):
    for offset in range(length):
        index = (y + offset) * img.width + x
        if index < len(img.pixels):
            if img.pixels[index]:
                return offset
    return length

    
def get_stroke_length(x_start, y_start, length):
    image_start_x = width / 2 - img.width / 2
    image_start_y = height / 2 - img.height / 2
    image_end_x = image_start_x + img.width
    image_end_y = image_start_y + img.height
    
    if x_start < image_start_x or x_start > image_end_x:
        return length
    elif y_start > image_start_y or y_start + length > image_start_y:
        return find_length(x_start - image_start_x, y_start - image_start_y, length)
    
    return length

    
def draw():
    padding = 8
    background(0, 0, 0)
    
    x_offset = padding
    while x_offset <= width - padding:
        y_offset = padding
        while y_offset < height - padding:
            length = get_stroke_length(x_offset, y_offset, random.choice(fib) * 2)
            if length:
                if y_offset + length > height - padding:
                    length = height - padding - y_offset
                elif height - padding - y_offset < 32:
                    length = height - padding - y_offset
                stroke(*random.choice(colors_array))
                line(x_offset, y_offset, x_offset, y_offset + length)
            y_offset += length + padding
        x_offset += padding
    
    
def keyPressed():
    k = str(key)
    if k == " ":
        redraw()
    elif k == "s":
        saveFrame("output.png")
        
    
