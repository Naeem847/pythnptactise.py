from turtle import *
import colorsys

# screen setup
Screen().bgcolor("black")
Screen().title("Tiktok Logo")
# turtle setup
tracer(3)
width(2)

# parameters
sides=7
length=5
rotation=7
steps=300

# color mode
colormode(1)
hue=0.0

for i in range(steps):
    # smooth rainbow color shift
    r,g,b=colorsys.hsv_to_rgb(hue,1.0,1.0)
    pencolor(r,g,b)
    # draw polygon
    for j in range(sides):
        forward((length + i) * 0.6)
        left(360/sides)
    # rotation and spiral outward
    left(rotation)
    hue +=0.01


done()