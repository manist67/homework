# author : Seung Min Lee
# since : 2023-03-25
# purpose : Calculate how many images store on given USB.

import math

# user input of USB Size
usb_size_gb = float(input("Enter USB size (GB): "))
usb_total_size = usb_size_gb * 1_000_000_000 # Separate for legible

image_resolution = 800 * 600 # image sizes are 800x600.

# Expressions of file size are image resolution * color depth * copression
GIF = image_resolution * 1 * 1/5 # image resolution * 8bits * 5:1
JPEG = image_resolution * 3 * 1/25 # image_resolution * 24bits * 25:1
PNG = image_resolution * 3 * 1/8 # image_resolution * 24bits * 8:1
TIFF = image_resolution * 6 * 1 # image_resolution * 48bits * (no compression == 1)

# print formatted results 
print("{:>5} images in GIF format can be stored".format( math.floor(usb_total_size / GIF) ))
print("{:>5} images in JPEG format can be stored".format( math.floor(usb_total_size / JPEG) ))
print("{:>5} images in PNG format can be stored".format( math.floor(usb_total_size / PNG) ))
print("{:>5} images in TIFF format can be stored".format( math.floor(usb_total_size / TIFF) ))