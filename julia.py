from PIL import Image
import random

cmin, cmax = -2.0, 1
dmin, dmax = -1.5, 1.5

imgc, imgd = 512, 512

maxIt = 256

image3 = Image.new("RGB", (imgc, imgd)) 

m = complex(random.random() * 2.0 - 1.0, random.random() - 0.5)

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

image3.show()





