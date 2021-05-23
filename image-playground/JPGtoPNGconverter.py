import sys
import os
from  PIL import Image

# file to run: python3 JPGtoPNGconverter.py Pokedex/ new/

# grab first and second argument: 
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# print(image_folder,output_folder)

#check if ( a folder) 'new/' exists, if not create
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Loop through Pokedex,
# convert images to png
for filename in os.listdir(image_folder):
    try:
        img = Image.open(f'{image_folder}{filename}')
        # clean_name, e= os.path.splitext(filename)
        clean_name = os.path.splitext(filename)[0]
        # save to the new folder
        img.save(f'{output_folder}{clean_name}.png',"png")
        # print('all done!')
    except OSError:
        print("cannot convert", filename)




