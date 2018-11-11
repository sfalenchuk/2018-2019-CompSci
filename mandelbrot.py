#Sasha
#3 Fractals
#10/25/18
#used atopon.org/mandel
#overall the project went really well, and was fun
#On my honor, I have neither given nor recieved unauthorized aid

from PIL import Image
import random

xmin, xmax = -0.883333333333, -0.591666666666
ymin, ymax = .1, .39166666666666

amin, amax = -0.34166666666666, 0.1833333333333
bmin, bmax = -1.09166666666666, -0.5666666666666

cmin, cmax = -2.0, 1
dmin, dmax = -1.5, 1.5

imgx, imgy = 512, 512
imga, imgb = 512, 512
imgc, imgd = 512, 512

maxIt = 256

image = Image.new("RGB", (imgx,imgy))
image2 = Image.new("RGB", (imga,imgb))
image3 = Image.new("RGB", (imgc, imgd)) 

m = complex(random.random() * 2.0 - 1.0, random.random() - 0.5)
for y in range(imgy):
	cy = y * (ymax-ymin) / (imgy-1) + ymin
	for x in range(imgx):
		cx = x * (xmax-xmin) / (imgx-1) + xmin
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c

		r = i
		g = (i*50)%256
		b = 256-i

		image.putpixel((x,y),(r,g,b))

for y in range(imgb):
	cy = y * (bmax-bmin) / (imgb-1) + bmin
	for x in range(imga):
		cx = x * (amax-amin) / (imga-1) + amin
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c

		r = i+50
		g = i%50
		b = 100-i

		image2.putpixel((x,y),(r,g,b))

for y in range(imgd):
	zy = y * (dmax - dmin) / (imgd - 1) + dmin
	for x in range(imgc):
		zx = x * (cmax - cmin) / (imgc - 1) + cmin
		z = complex(zx, zy)
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + m

			r = i
			g = (i-5)
			b = i*50


			image3.putpixel((x,y),(b+0+r*65536))

image.show()

image2.show()
 
image3.show()
