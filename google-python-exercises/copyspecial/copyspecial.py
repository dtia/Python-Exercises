#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir:
      copy_to(get_files('.'), todir)
      sys.exit(1)

  if tozip:
      filestring = ' '.join(get_files(args))
      intro = 'Command I\'m going to do:' 
      command = "zip -j %s %s" % (tozip, filestring)
      print intro + command

      (status, output) = commands.getstatusoutput(command)
      if status:
          sys.stderr.write(output)
          sys.exit(1)

      print output
      sys.exit(1)
 
  print '\n'.join(get_files(args))  

def get_files(args):
    files = []
    for dir in args:
        filenames = os.listdir(dir)
        if filenames:
            for file in filenames:
                match = re.search(r'__(\w+)__', file)
                if match:
                    files.append(os.path.abspath(file))
    
    return files

def copy_to(paths, dir):
    for path in paths:
        shutil.copy(path, dir)


if __name__ == "__main__":
  main()
