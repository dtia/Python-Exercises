"""
Thumbtack Coding Challenge
Problem 3: Simple Database
Author: Derek Tia
"""
def main():
  com_dict = {}
  set = 'SET'
  get = 'GET'
  unset = 'UNSET'
  equalto= 'EQUALTO'
  end = 'END'
  begin = 'BEGIN'
  rollback = 'ROLLBACK'
  commit = 'COMMIT'
  
  commandline = raw_input('')
  command_arr = commandline.split()
  command = command_arr[0]
  
  global blocks
  global dict
  blocks = []
  dict = {}
  output = []

  while(command != end):
    if command == set:
      var, val = command_arr[1:]
      set_dict(var, val)
    
    elif command == get:
      var = command_arr[1]
      get_dict(var)

    elif command == unset:
      var = command_arr[1]
      unset_dict(var)

    elif command == equalto:
      val = command_arr[1]
      equalto_call(val)

    elif command == begin:
      begin_call() 

    elif command == rollback:
      rollback_call()

    elif command == commit:
      commit_blocks()
    
    commandline = raw_input('')
    command_arr = commandline.split()
    command = command_arr[0]

def begin_call():
  if len(blocks) > 0:
    # copy existing values over
    last_dict = blocks[len(blocks)-1].copy()
    if len(last_dict) > 0:
      blocks.append(last_dict)
  elif len(dict) > 0:
      blocks.append(dict)
  else:
    temp_dict = {}
    blocks.append(temp_dict)

def rollback_call():
  if len(blocks) > 0:
    blocks.pop()
  else:
    print 'INVALID ROLLBACK'

# traverse through blocks from beginning and save values to global dict
def commit_blocks():
  global blocks
  for block in blocks:
    for k, v in block.items():
      dict[k] = v
  blocks = []

def equalto_call(val):
  # if there is an open block
  if len(blocks) > 0:
    last_dict = blocks[len(blocks)-1] 
    print find_keys(val, last_dict) 
  else:
    print find_keys(val, dict)

def set_dict(var, val):
  # if there is an open block
  if len(blocks) > 0:
    last_dict = blocks[len(blocks)-1]
    set_val(var, val, last_dict)
  else:
    set_val(var, val, dict)

def set_val(var, val, dict):
  dict[var] = val

def get_dict(var):
  # if there is an open block
  if len(blocks) > 0:
    last_dict = blocks[len(blocks)-1] 
    print_val(var, last_dict)
  else:
    print_val(var, dict)

def print_val(var, dict):
  if var in dict:
    print dict[var]
  else:
    print 'NULL'

def unset_dict(var):
  # if there is an open block
  if len(blocks) > 0:
    last_dict = blocks[len(blocks)-1]
    unset_var(var, last_dict)
  else:
    unset_var(var, dict)

def unset_var(var, dict):    
  if var in dict:
    del dict[var]

def find_keys(val, dict):
  matches = []
  for k, v in dict.items():
    if v == val:
      matches.append(k)
  
  if len(matches) == 0:
    output = 'NONE'
  else:
    output = ' '.join(sorted(matches)) #sort by alphabetical order

  return output
  
if __name__ == '__main__':
  main()
