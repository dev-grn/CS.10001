from cs1media import *

# This code converts an image into a black & white poster.

threshold = 160
white = (255, 255, 255)
black = (0, 0, 0)

image = load_picture('./images/minion.jpg')
width, height = image.size()

for y in range(height):
    for x in range(width):
        r, g, b = image.get(x, y)
        average_brightness = (r + g + b) // 3
        if average_brightness > (2 / 3) * threshold:
            image.set(x, y, (255, 255, 0))
        elif average_brightness < (1 / 3) * threshold:
            image.set(x, y, (0, 0, 255))
        else:
            image.set(x, y, (0, 255, 0))
     
image.show()
