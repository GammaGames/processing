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

def setup():
    random.seed()
    colorMode(HSB, 360, 100, 100)
    strokeWeight(5)
    strokeCap(ROUND)
    noLoop()
    
    size(1000, 500)

    
def draw():    
    background(0, 0, 0)
    
    x_offset = width * -1
    while x_offset < width:
        cur_x_offset = x_offset
        y_offset = 0
        while y_offset < height:
            stroke(*random.choice(colors_array))
            length = random.randint(15, 60)
            line(cur_x_offset, y_offset, cur_x_offset + length / 2, y_offset + length)
            y_offset += length + 10
            cur_x_offset += length / 2 + 5
        x_offset += 12
    saveFrame("output.png")
