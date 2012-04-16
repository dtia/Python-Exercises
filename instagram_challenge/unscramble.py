# coding: utf-8
from PIL import Image
import urllib
import os
import math

def main():
  img_url = 'http://instagram-static.s3.amazonaws.com/images/TokyoPanoramaShredded.png'
  
  ufile = urllib.urlopen(img_url)
  info = ufile.info()
  img_file = './shredded.png'
  output_img_file = 'unshredded.jpg'

  if not os.path.exists(os.path.abspath(img_file)):
    if info.gettype() == 'image/png':
      print 'Retrieving ' + img_file + ' ...'
      urllib.urlretrieve(img_url, img_file) 
  
  if os.path.exists(os.path.abspath(output_img_file)):
    os.remove(output_img_file)

  image = Image.open(img_file)
  width, height = image.size
  print 'width: %s height: %s' % (width, height)
  data = image.getdata() # This gets pixel data
  
  # Access an arbitrary pixel. Data is stored as a 2d array where rows are
  # sequential. Each element in the array is a RGBA tuple (red, green, blue,
  # alpha).
  #x, y = 20, 90
  def get_pixel_value(x, y):
    pixel = data[y * width + x]
    return pixel
  #print get_pixel_value(20, 30)

  # Create a new image of the same size as the original
  # and copy a region into the new image
  NUMBER_OF_COLUMNS = 10
  unshredded = Image.new("RGBA", image.size)
  shred_width = unshredded.size[0]/NUMBER_OF_COLUMNS
  shred_number = 0 
  x1, y1 = shred_width * shred_number, 0
  x2, y2 = x1 + shred_width, height
  source_region = image.crop([x1, y1, x2, y2])
  destination_point = (0, 0)
  unshredded.paste(source_region, destination_point)
  # Output the new image
  unshredded.save(output_img_file, "JPEG")

  strip1 = 0, 0, 0, 0
  strip2 = 1, 1, 1, 1
  def compare_strips(strip1, strip2):
    lx_1, ly_1, rx_1, ry_1 = strip1
    lx_2, ly_2, rx_2, ry_2 = strip2
    
    height_inc = height / 10
    height_marker = 0
    for height_marker in range(0, height, height_inc):
      #print get_pixel_value(lx_1, height_marker)
      # compare left of A to right of B
      diff1 = subtract_rgb(get_pixel_value(lx_1, height_marker), get_pixel_value(rx_2, height_marker))
      # compare right of A to left of B
      diff2 = subtract_rgb(get_pixel_value(rx_1, height_marker), get_pixel_value(lx_2, height_marker))
      # check threshold
      print 'diff 1: ' + str(diff1)
      print 'diff 2: ' + str(diff2)

  def subtract_rgb(rgb1, rgb2):
    dr = rgb1[0] - rgb2[0]
    dg = rgb1[1] - rgb2[1]
    db = rgb1[2] - rgb2[2]
    da = rgb1[3] - rgb2[3]
    
    norm_diff = math.sqrt(math.pow(dr, 2) + math.pow(dg, 2) + math.pow(db, 2) + math.pow(da, 2))
    return (dr, dg, db, da, norm_diff)

  compare_strips(strip1, strip2)

if __name__ == '__main__':
  main()
