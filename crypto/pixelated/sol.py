from PIL import Image, ImageDraw
import operator
import os, sys

if len(sys.argv)!=3:
    print("This takes two arguments")
    exit()
infile_A=str(sys.argv[1])
infile_B=str(sys.argv[2])

if not os.path.isfile(infile_A):
    print(sys.argv[1]+"does not exist")
    exit()

if not os.path.isfile(infile_B):
    print(sys.argv[2]+"does not exist")
    exit()

img_A=Image.open(infile_A)
img_B=Image.open(infile_B)

out_file="decrypted_file"

width = img_A.size[0]
height = img_A.size[0]
out_image=Image.new('RGB', (width, height))
draw_image= ImageDraw.Draw(out_image)

for x in range(0, width):
    for y in range(0, height):
        pixel_A=img_A.getpixel((x,y))
        pixel_B=img_B.getpixel((x,y))
        pixel_mixed = tuple((pixel_A[0]^pixel_B[0],pixel_A[1]^pixel_B[1],pixel_A[2]^pixel_B[2]))
        print(pixel_mixed)
        if pixel_mixed == (255,255,255):
            pixel_mixed = (0,0,0)
        draw_image.point((x,y), pixel_mixed)

out_image.save(out_file, 'PNG')
print("Done")
