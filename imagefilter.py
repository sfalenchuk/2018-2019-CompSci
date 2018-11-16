from PIL import Image
# import scipy.misc as smp
image = "image.jpeg"
img = Image.open(image)

pix = img.load()
x = 1
y = 1

# pixtwo = Image.new

while x < img.size[0]-1:

	while y < img.size[1]-1:
	
		pix[x,y] = (255,0,0)
		# pix[x,y] = (255,255,255)

		y = y+2
	y = 1
	x = x+1

# img = smp.toimage( pix )
img.show()
# pixtwo.sshow()
