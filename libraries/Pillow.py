from PIL import Image

image_path = "R:\\WALLPAPER\\IMG_20200915_165037.jpg"
image_file = Image.open(image_path)

image_file.save("R:\\WALLPAPER\\" + "test.jpg", quality=95)

image_file.save("R:\\WALLPAPER\\" + "test2.jpg", quality=50)

image_file.save("R:\\WALLPAPER\\" + "test3.jpg", quality=25)
