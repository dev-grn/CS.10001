from cs1media import *

# This code converts an image into a black & white poster.

threshold = 100
white = (255, 255, 255)
black = (0, 0, 0)

image = load_picture('./images/minion.jpg')
width, height = image.size()

for y in range(height):
    for x in range(width):
        r, g, b = image.get(x, y)
        image.set(x, y, (255 - r, 255 - g, 255 - b))
            
image.show()
