#!/usr/bin/env python
# -*- coding: utf-8 -*-

 
import sys
 

from cStringIO import StringIO
from PIL import Image as pil
 

 

 
def compress_image(pic):
	input_file = StringIO(pic.get_contents_as_string())
    img = pil.open(input_file)
    tmp = StringIO()
    img.save(tmp, 'JPEG', quality=80)
    tmp.seek(0)
    output_data = tmp.getvalue()
 
    headers = dict()
    headers['Content-Type'] = 'image/jpeg'
    headers['Content-Length'] = str(len(output_data))
    pic.set_contents_from_string(output_data, headers=headers, policy='public-read')
    
    tmp.close()
    input_file.close()
 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'dry_run':
            start_compressing(dry_run=True)
        else:
            print 'Invalid command. For a dry run please run: python compress_s3_images.py dry_run'
    else:
        compress_image("img.png")
    sys.exit()
