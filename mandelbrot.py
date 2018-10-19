from PIL import Image

imgx = 512
imgy = 512
z1 = [0,0]
z = [x,y]
x = 0
x1 = 0
y = 0
y1 = 0

image = Image.new("RGB", (imgx, imgy))

def mandelbrot():

	abs(z) = sqrt((x^2)+(y^2))
	z1 * z = [x1,y1]*[x2,y2]

while(x<=511):
	while(y<=511):
		image.putpixel((x,y),(255,0,0))
		def mandelbrot


image.save("mandelbrot.png","PNG")