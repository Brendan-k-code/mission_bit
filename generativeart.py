from PIL import Image, ImageDraw
image = Image.open('sample_image.gif')
resized_image = image.resize((200,200))

class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes # store the dictionary

    def draw(self, draw_context):
        x, y = self.attributes['position']
        x2,y2 = self.attributes['position2']
        x3,y3 = self.attributes['position3']
        r = self.attributes['radius']
        size = self.attributes['size']
        color = self.attributes['color']
        color2 = self.attributes['color2']
        draw_context.ellipse([(x - r, y - r), (x + r, y + r)],
        fill=color)
        draw_context.rectangle((x2-size, y2-size, x2 + size,y2 + size), fill=color2) #for rectangles
       
        draw_context.ellipse([(x3 - r, y3 - r), (x3 + r, y3 + r)],
        fill=color)
        draw_context.rectangle((x3, y3, x3 + r,y3+ r), fill=color)        #for speech bubble things

class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height),background_color)

    def add_element(self, element):
        self.elements.append(element)
    
    def render(self):
        draw = ImageDraw.Draw(self.image)
        for element in self.elements:
            element.draw(draw)
            self.image.show()
            self.image.save("output.png")

import random

def main():
    canvas = Canvas(1000,1000, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    for _ in range(20):
        attrs = {
            'position': (random.randint(0, 1000), random.randint(0,1000)),
            'position2':(random.randint(0, 1000), random.randint(0,1000)),
            'position3': (random.randint(0, 1000), random.randint(0,1000)),
            'radius': random.randint(10, 200),
            'color': (random.randint(0,255), random.randint(0,255),random.randint(0,255)),
            'color2':(random.randint(0,255), random.randint(0,255),random.randint(0,255)),
            'size': random.randint(5, 100),
            }
        circle = ArtElement(attrs)
        canvas.add_element(circle)
    canvas.render()


main()

canvas_image = Image.open("output.png") 
canvas_image.paste(resized_image, (800, 800))
canvas_image.save("image_on_canvas.png")
print("Image successfully added to canvas and saved as 'image_on_canvas.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas1.png")
print("Image successfully added to canvas and saved as 'image_on_canvas1.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas1.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas2.png")
print("Image successfully added to canvas and saved as 'image_on_canvas2.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas2.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas3.png")
print("Image successfully added to canvas and saved as 'image_on_canvas3.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas3.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas4.png")
print("Image successfully added to canvas and saved as 'image_on_canvas4.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas4.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas5.png")
print("Image successfully added to canvas and saved as 'image_on_canvas5.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas5.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas6.png")
print("Image successfully added to canvas and saved as 'image_on_canvas6.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas6.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas7.png")
print("Image successfully added to canvas and saved as 'image_on_canvas7.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas7.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas8.png")
print("Image successfully added to canvas and saved as 'image_on_canvas8.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas8.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas9.png")
print("Image successfully added to canvas and saved as 'image_on_canvas9.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas9.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas10.png")
print("Image successfully added to canvas and saved as 'image_on_canvas10.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas10.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas11.png")
print("Image successfully added to canvas and saved as 'image_on_canvas11.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas11.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas12.png")
print("Image successfully added to canvas and saved as 'image_on_canvas12.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas12.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas13.png")
print("Image successfully added to canvas and saved as 'image_on_canvas13.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas13.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas14.png")
print("Image successfully added to canvas and saved as 'image_on_canvas14.png'")
canvas_image.show()

canvas_image = Image.open("image_on_canvas14.png") 
canvas_image.paste(resized_image, (random.randint(0,1000),(random.randint(0,1000))))
canvas_image.save("image_on_canvas15.png")
print("Image successfully added to canvas and saved as 'image_on_canvas15.png'")
canvas_image.show()



