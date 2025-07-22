from PIL import Image

# 1. Open the image to add
try:
    image_to_add = Image.open("sample_image.gif") # Make sure this file exists
except FileNotFoundError:
    print("Error: 'example_image.png' not found. Please create or provide a valid image file.")
    exit()

# 2. Create the canvas image

canvas_image = Image.open("output.png") 

# 3. Paste the image onto the canvas
x_coord = 900
y_coord = 900
canvas_image.paste(image_to_add, (x_coord, y_coord))

# 4. Save the result
canvas_image.save("image_on_canvas.png")
print("Image successfully added to canvas and saved as 'image_on_canvas.png'")

# Optional: Display the image
# canvas_image.show()