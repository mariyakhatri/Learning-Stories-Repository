from PIL import Image

# Open the image file
image_path = "your_image.jpg"  # Replace with your image file path
img = Image.open(image_path)

# Ask user for rotation angle
angle = float(input("Enter rotation angle in degrees (e.g. 90, 180, 270): "))

# Rotate the image
rotated_img = img.rotate(angle, expand=True)

# Show the rotated image
rotated_img.show()

# Optionally save it
save_path = "rotated_image.jpg"
rotated_img.save(save_path)
print(f"Image rotated by {angle}° and saved as '{save_path}'")
