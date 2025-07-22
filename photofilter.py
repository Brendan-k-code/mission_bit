from PIL import Image
image = Image.open('sample_image.gif')
image.show()

resized_image = image.resize((100,100))
resized_image.show()

grayscale_image = image.convert('L')
grayscale_image.show()

rotated_image = image.rotate(90)
rotated_image.show()

test_image = image.effect_spread(20)
test_image.show()

test_image1 = image.effect_spread(150) 
test_image1.show()

resized_image.save('resized.png')
rotated_image.save('rotated.png')
grayscale_image.save('grayscale.png')
test_image.save('smudged.png')
test_image1.save('exploded.png')