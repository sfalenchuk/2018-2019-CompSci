from PIL import Image
image = "image.jpeg"
img = Image.open(image)

pix = img.load()
x = 1
y = 1

pixtwo = Image.new

while x < img.size[0]-1:

	while y < img.size[1]-1:
	
		pix[x,y] = (255,255,255)
		pix[x,y] = (255,255,255)

		y = y+2
	x = x+2


pixtwo.save("filter.png") 
pixtwo.show.show()
