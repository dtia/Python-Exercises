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
  global width
  global height
  global data
  width, height = image.size
  print 'width: %s height: %s' % (width, height)
  data = image.getdata() # This gets pixel data
  
  # Create a new image of the same size as the original
  # and copy a region into the new image
  TOLERANCE = 50
  NUMBER_OF_COLUMNS = 20
  unshredded = Image.new("RGBA", image.size)
  shred_width = unshredded.size[0]/NUMBER_OF_COLUMNS

  current_avg = ''
  first_strip = (0, 0, shred_width, height)
  for shred_number in range(1, NUMBER_OF_COLUMNS):
    x1, y1 = shred_width * shred_number, 0
    x2, y2 = x1 + shred_width, height
    # compare first strip with current strip in loop
    current_strip = (x1, y1, x2, y2)
    (avg_diff, orientation) = compare_strips(first_strip, current_strip)
    
    if current_avg == '' or avg_diff < current_avg:
      current_avg = avg_diff
      print 'strip: %s current avg: %s' % (shred_number, current_avg)

    #if avg_diff < TOLERANCE:     
      #if orientation == 1:
    print current_strip
    print 'avg diff: %s orientation: %s' % (avg_diff, orientation)
    # create new image with strip in correct place
    # repeat process


  source_region = image.crop([x1, y1, x2, y2])
  destination_point = (0, 0)
  unshredded.paste(source_region, destination_point)
  # Output the new image
  unshredded.save(output_img_file, "JPEG")

# Access an arbitrary pixel. Data is stored as a 2d array where rows are
# sequential. Each element in the array is a RGBA tuple (red, green, blue,
# alpha).
#x, y = 20, 90
def get_pixel_value(x, y):
  pixel = data[y * width + x]
  return pixel

def compare_strips(strip1, strip2):
  lx_1, ly_1, rx_1, ry_1 = strip1
  lx_2, ly_2, rx_2, ry_2 = strip2

  # Orientation 1: A B
  # Orientation 2: B A
  norm_list1 = []
  norm_list2 = []
  
  height_inc = height / 10
  height_marker = 0  
  for height_marker in range(0, height, height_inc):
    # compare left of A to right of B (Orientation 2)
    dr1, dg1, db1, da1, dn1 = subtract_rgb(get_pixel_value(lx_1, height_marker), get_pixel_value(rx_2, height_marker))
    # compare right of A to left of B (Orientation 1)
    dr2, dg2, db2, da2, dn2 = subtract_rgb(get_pixel_value(rx_1, height_marker), get_pixel_value(lx_2, height_marker))
    
    norm_list1.append(dn1)
    norm_list2.append(dn2)

  avg1 = get_avg(norm_list1)
  avg2 = get_avg(norm_list2)
  
  print 'avg 1: %s avg 2: %s' % (avg1, avg2)
  
  if avg1 > avg2:
    return (avg2, 1) # Orientation 1
  else:
    return (avg1, 2) # Orientation 2

def get_avg(list):
  sum = 0
  for num in list:
    sum += num
  return sum / len(list)

def subtract_rgb(rgb1, rgb2):
  dr = rgb1[0] - rgb2[0]
  dg = rgb1[1] - rgb2[1]
  db = rgb1[2] - rgb2[2]
  da = rgb1[3] - rgb2[3]
  
  norm_diff = math.sqrt(math.pow(dr, 2) + math.pow(dg, 2) + math.pow(db, 2) + math.pow(da, 2))
  return (dr, dg, db, da, norm_diff)

if __name__ == '__main__':
  main()
