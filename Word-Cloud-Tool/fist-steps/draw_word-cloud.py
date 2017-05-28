# Python 2
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
from random import randint



image = Image.new("RGB", (1200,530), (0, 10, 30))
draw = ImageDraw.Draw(image)


# Cyan
r = [10]
g = [255]
b = [255]
clourindex = 0




wordlist = ["Sonne", "Mond", "Sterne", "Kind", "Musik", "Tanz", "Affe", "Theater", "Schwimmbad", "Puppe", "Auge", "Auto", "Fahrrad", "Zahn", "Motor", "Haare", "Figur", "Mode", "Kreis", "Stadt", "Kultur", "Bewegung", "Tour", "Disziplin", "Studium", "Arzt", "Haus", "Mobil", "Garten", "Schiff", "Anlage", "Ohr", "Mund", "Schokolade", "Zucker", "Schirm", "Film", "Zitrone", "Mango", "Apfel"]
counts = [70, 70, 67, 65, 60, 60, 58, 55, 53, 50, 50, 50, 47, 45, 42, 40, 40, 38, 35, 32, 32, 30, 30, 25, 20, 20, 20, 15, 12, 10, 10, 10, 10, 10, 7, 7, 5, 5, 5, 5]
fontweights = [50]
index = 1
z = float(fontweights[0])/counts[0]
while index < len(counts):
	x = counts[index] * z
	y = int(x) + 10
	fontweights.append(y)
	index = index + 1



counter = 0

while counter < len(wordlist):
	fontsize = fontweights[counter]
	font = ImageFont.truetype('Trebuchet MS.ttf', fontsize)
	text = wordlist[counter] + "(" + str(int(counts[counter])) + ")"
	width, height = font.getsize(text)
	draw.text((randint(30, 940), randint(30, 450)), wordlist[counter] + "(" + str(int(counts[counter])) + ")", font=font, fill=(r[clourindex],g[clourindex],b[clourindex]))
	counter = counter + 1


image.show()
image.save("pic.png")
