import cv2

# list of ascii characters used when convert image to ascii text
CHARS = ' .,-~:;=!*#$@' # 13

# number of pixels in one line, new_width = 100
nw = 100

#image read
img = cv2.imread('./{image_name_spaece}.jpg')

#convert color BGR2GRAY
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = img.shape
nh = int(h / w * nw)
img = cv2.resize(img, (nw * 2, nh))

for row in img:

	for pixel in row: # pixel 0-255 -> CHARS 0-12
        index = int(pixel / 256 * len(CHARS))
        print(CHARS[index], end='')
    print()
