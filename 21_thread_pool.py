import time, random

file_list = [
    "image_0001.jpg",
    "image_0002.jpg",
    "image_0003.jpg",
    "image_0004.jpg",
    "image_0005.jpg",
    "image_0006.jpg",
    "image_0007.jpg",
    "image_0008.jpg",
    "image_0009.jpg",
    "image_0010.jpg"
]

def image_converter(image):
    print(f"Converting {image}...")
    time.sleep(random.randint(1,4))
    print(f"{image} finished.")

for i in file_list:
    image_converter(i)