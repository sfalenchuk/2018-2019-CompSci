from PIL import Image

imgx = 512
imgy = 512
x = 0
y = 0

image = Image.new("RGB", (imgx, imgy))

while(x<=511):
	while(y<=511):
		image.putpixel((x,y),(255,0,0))
		y = y+1
	x = x+1
	y=0


image.save("demo.png","PNG")
