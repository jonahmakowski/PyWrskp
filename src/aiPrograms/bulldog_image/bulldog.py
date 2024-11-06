from PIL import Image, ImageDraw, ImageEnhance

# Create a new image with a white background
image = Image.new('RGB', (500, 500), 'white')

# Get a drawing context
draw = ImageDraw.Draw(image)

# Create a gradient fill for the collar
collar_gradient = Image.new('RGB', (300, 150))
for x in range(300):
    for y in range(150):
        collar_gradient.putpixel((x, y), (255, int(x/1.2), 0))

# Draw the body
draw.rectangle((100, 350, 400, 500), fill=(139, 69, 19), outline='black')

# Draw the head
draw.ellipse((100, 50, 400, 350), fill=(139, 69, 19), outline='black')

# Draw the ears
draw.polygon([(50, 100), (75, 50), (100, 100)], fill=(139, 69, 19), outline='black')
draw.polygon([(450, 100), (425, 50), (400, 100)], fill=(139, 69, 19), outline='black')

# Draw the eyes
draw.ellipse((150, 150, 200, 200), fill='white', outline='black')
draw.ellipse((300, 150, 350, 200), fill='white', outline='black')
draw.ellipse((155, 155, 195, 195), fill='black', outline='black')
draw.ellipse((305, 155, 345, 195), fill='black', outline='black')

# Draw the nose
draw.polygon([(250, 200), (300, 250), (250, 300)], fill='black', outline='black')
draw.polygon([(245, 195), (295, 245), (245, 295)], fill='lightgrey', outline='black')

# Draw the mouth
draw.arc((150, 250, 350, 350), 0, 180, fill='black')
draw.line((165, 325, 335, 325), fill='white', width=3)

# Draw the collar
draw.bitmap((100, 500), collar_gradient, fill='red')

# Draw the shadow
draw.ellipse((105, 505, 395, 755), fill='black', outline='black')

# Save the image
image.save('bulldog5.jpg')

