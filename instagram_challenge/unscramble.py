# coding: utf-8
from PIL import Image
import urllib
import os

def main():
  img_url = 'http://instagram-static.s3.amazonaws.com/images/TokyoPanoramaShredded.png'
  
  ufile = urllib.urlopen(img_url)
  info = ufile.info()
  img_file = 'shredded.png'

  if not os.path.exists(os.path.abspath(img_file)):
    if info.gettype() == 'image/png':
      print 'Retrieving ' + img_file + ' ...'
      urllib.urlretrieve(img_url, './' + img_file) 

  image = Image.open(img_file)
  width, height = image.size
  print 'width: %s height: %s' % (width, height)
  data = image.getdata() # This gets pixel data
  
  # Access an arbitrary pixel. Data is stored as a 2d array where rows are
  # sequential. Each element in the array is a RGBA tuple (red, green, blue,
  # alpha).
  x, y = 20, 90
  def get_pixel_value(x, y):
    pixel = data[y * width + x]
    return pixel
  print get_pixel_value(20, 30)

  # Create a new image of the same size as the original
  # and copy a region into the new image
  NUMBER_OF_COLUMNS = 5
  unshredded = Image.new("RGBA", image.size)
  shred_width = unshredded.size[0]/NUMBER_OF_COLUMNS
  shred_number = 1
  x1, y1 = shred_width * shred_number, 0
  x2, y2 = x1 + shred_width, height
  source_region = image.crop([x1, y1, x2, y2])
  destination_point = (0, 0)
  unshredded.paste(source_region, destination_point)
  # Output the new image
  unshredded.save("unshredded.jpg", "JPEG")

if __name__ == '__main__':
  main()
