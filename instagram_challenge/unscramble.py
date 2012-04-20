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
  global output_img_file
  output_img_file = 'unshredded.jpg'

  if not os.path.exists(os.path.abspath(img_file)):
    if info.gettype() == 'image/png':
      print 'Retrieving ' + img_file + ' ...'
      urllib.urlretrieve(img_url, img_file) 
  
  if os.path.exists(os.path.abspath(output_img_file)):
    os.remove(output_img_file)

  global image
  global width
  global height
  global data

  image = Image.open(img_file)
  width, height = image.size
  print 'width: %s height: %s' % (width, height)
  data = image.getdata() # This gets pixel data
  
  # Create a new image of the same size as the original
  # and copy a region into the new image
  TOLERANCE = 50
  global NUMBER_OF_COLUMNS
  NUMBER_OF_COLUMNS = 20
  unshredded = Image.new("RGBA", image.size)
  global shred_width
  shred_width = unshredded.size[0]/NUMBER_OF_COLUMNS

  current_avg = ''
  matched_strip = ''
  matched_strip_num = '' 
  first_strip = (0, 0, shred_width, height)
  for shred_number in range(1, NUMBER_OF_COLUMNS):
    x1, y1 = shred_width * shred_number, 0
    x2, y2 = x1 + shred_width, height
    # compare first strip with current strip in loop
    current_strip = (x1, y1, x2, y2)
    (avg_diff, orientation) = compare_strips(first_strip, current_strip)
    
    if (current_avg == '' or avg_diff < current_avg) and avg_diff != 0:
      current_avg = avg_diff
      matched_strip = current_strip
      matched_strip_num = shred_number
      print 'strip: %s current avg: %s' % (shred_number, current_avg)
      

    #if avg_diff < TOLERANCE:     
      #if orientation == 1:
  print 'avg diff: %s orientation: %s current strip: %s strip num: %s' % (current_avg, orientation, str(matched_strip), matched_strip_num)
    # create new image with strip in correct place
    # repeat process
  insert_neighbor_strips(first_strip, matched_strip, orientation, unshredded)


def insert_neighbor_strips(strip1, strip2, orientation, img):
  # swap first strip with matched strip + 1 if orientation B, otherwise swap with matched strip - 1
    if orientation == 1:
      # A B
      insert_strip(strip1, img, (strip2[0] - shred_width, 0))
      insert_strip(strip2, img, (strip2[0], 0))
      insert_strip([strip2[0] - shred_width, 0, strip2[0], height], img, (0,0))
    else:
      # B A
      insert_strip(strip1, img, (strip2[0] + shred_width, 0))
      insert_strip(strip2, img, (strip2[0], 0))
      insert_strip([strip2[0] + shred_width, 0, strip2[0], height], img, (0,0))
  
    #for shred_number in range(1, NUMBER_OF_COLUMNS):
      # insert rest of strips here

def insert_strip(strip, img, destination_point):
  #source_region = image.crop([x1, y1, x2, y2])
  source_region = image.crop(strip)
  img.paste(source_region, destination_point)
  # Output the new image
  img.save(output_img_file, "JPEG")

# Access an arbitrary pixel. Data is stored as a 2d array where rows are
# sequential. Each element in the array is a RGBA tuple (red, green, blue,
# alpha).
def get_pixel_value(x, y):
  pixel = data[y * width + x]
  return pixel

def compare_strips(strip1, strip2):
  lx_1, ly_1, rx_1, ry_1 = strip1
  lx_2, ly_2, rx_2, ry_2 = strip2

  #print lx_1, ly_1, rx_1, ry_1
  #print lx_2, ly_2, rx_2, ry_2 

  # Orientation 1: A B
  # Orientation 2: B A
  norm_list1 = []
  norm_list2 = []
  
  height_inc = height / 10
  height_marker = 0  
  for height_marker in range(0, height-height_inc, height_inc):
    # compare left of A to right of B (Orientation 2)
    dr1, dg1, db1, da1, dn1 = subtract_rgb(get_pixel_value(lx_1 + 1, height_marker), get_pixel_value(rx_2 - 1, height_marker))
    # compare right of A to left of B (Orientation 1)
    print 'first pixel: %s second pixel: %s' % (str(get_pixel_value(rx_1 - 1, height_marker)), str(get_pixel_value(lx_2 + 1, height_marker)))
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
