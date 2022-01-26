from os import listdir
from pathlib import Path
from PIL import Image,ExifTags

input_dir = '{}{}'.format(Path(__file__).parent,'''\\''')
output_dir = '{}{}'.format(Path(__file__).parent,'''\\output_img\\''')

Path(output_dir).mkdir(parents=True, exist_ok=True)

# Skala zmniejszenia
###############################################

factor=5

###############################################

def rot(im):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        
        exif = dict(im._getexif().items())
        if exif[orientation] == 3:
            im=im.rotate(180, expand=True)
        elif exif[orientation] == 6:
            im=im.rotate(270, expand=True)
        elif exif[orientation] == 8:
            im=im.rotate(90, expand=True)

        return im
    except (AttributeError, KeyError, IndexError):
        return im

for x in listdir(input_dir):
    if not x.endswith('.jpg') and not x.endswith('.png'):
        continue    
    im = Image.open(input_dir+x)
    im=rot(im)
    new_size=(i//factor for i in im.size)
    im_new=im.resize(new_size,Image.ANTIALIAS)        
    # im_new.show()
    im_new.save(output_dir+x, quality=90, optimize=True)