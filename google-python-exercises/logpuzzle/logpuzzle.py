#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  f = open(filename, 'rU')
  images = re.findall(r'GET\s(\S+/puzzle/\S+)\sHTTP', f.read())
  paths = {}
  extractfile = re.search(r'\S_(\S+)', filename)
  baseurl = ''

  if extractfile:
    baseurl = extractfile.group(1)

  for image in images:

    if image not in paths:
      paths[image] = 'http://' + baseurl + image
  
  return sorted(paths.values(), key=get_key)

def get_key(filename):
  match = re.search(r'-\S+-(\S+)', filename)
  if match:
    return match.group(1)

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(os.path.abspath(dest_dir)):
    os.mkdir(dest_dir)

  imglist = []
  file_ext = 0
  for img_url in img_urls:
    ufile = urllib.urlopen(img_url)
    info = ufile.info()
    if info.gettype() == 'image/jpeg':
      imgfile = 'img' + str(file_ext) + '.jpg'
      print 'Retrieving ' + imgfile + ' ...'
      urllib.urlretrieve(img_url, dest_dir + '/' + imgfile) 
      file_ext += 1
      imglist.append(imgfile)
  
  create_html_file(imglist, dest_dir)

def create_html_file(imglist, dest_dir):
  imagestitch = open(dest_dir + '/index.html', 'w')  
  imagestitch.write('<verbatim>')

  for img in imglist:
    imagestitch.write('<img src=\'' + img + '\'>')
  
  imagestitch.write('</verbatim>')
  imagestitch.close()


def main():
  args = sys.argv[1:]
  
  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  
  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
