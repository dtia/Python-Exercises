import csv
import datetime
import os

def main():
  property_file = 'properties.csv'
  calendar_file = 'calendar.csv'
  search_file = 'searches.csv'
  search_output = 'search_results.csv'
  
  properties_reader = csv.reader(open(property_file, 'rb'), delimiter=',')
  calendar_reader = csv.reader(open(calendar_file, 'rb'), delimiter=',')
  search_reader = csv.reader(open(search_file, 'rb'), delimiter=',')
  output_writer = csv.writer(open(search_output, 'w'), delimiter=',')

  properties = {}
  for property in properties_reader:
    (index, xcoord, ycoord, price) = property
    if (xcoord, ycoord) not in properties: properties[(xcoord, ycoord)] = (index, price)
  
  print 'Generating Results ...'
  
  for search in search_reader:
    (index, xcoord, ycoord, arrive, leave) = search
    location_filtered = filter_location(xcoord, ycoord, properties)
    date_price_filtered = filter_date_get_price(index, arrive, leave, calendar_reader, location_filtered)
   
    final_sorted = {}
    if date_price_filtered:
      final_sorted = sorted(date_price_filtered, key=lambda item: date_price_filtered[item][2])
      rank = 1
      for final_prop_k in final_sorted[:10]:
        (prop_index, price, total_price) = date_price_filtered[final_prop_k]
        # output: search_id, rank, prop_id, total_price 
        output_writer.writerow([index, rank, prop_index, total_price])
        rank += 1

    else:
      # no matches
      output_writer.writerow([index, '-', '-', '-'])
    

  print 'Done!'

def filter_location(xcoord, ycoord, properties):
  filtered_prop = {}
  
  for property in properties.keys():
    (xprop, yprop) = property

    if float(xcoord) - 1 <= float(xprop) and float(xprop) <= float(xcoord) + 1 and \
       float(ycoord) - 1 <= float(yprop) and float(yprop) <= float(ycoord) + 1:
      filtered_prop[property] = properties[property]
  
  return filtered_prop

def filter_date_get_price(search_index, search_date_arrive, search_date_leave, calendar_reader, properties):
  total_price = -1
  for k, v  in properties.items():
    (prop_index, price) = v  
    (date_diff, date_list) = get_date_range(search_date_arrive, search_date_leave)

    if date_diff > 0:
      #print 'arrive: ' + search_date_arrive + ' leave: ' + search_date_leave + ' diff: ' + str(date_diff)
      total_price = get_special_price(prop_index, date_list, price, calendar_reader)
      properties[k] = (prop_index, price, total_price)
    else:
      # Negative number of days! so no price
      properties[k] = (prop_index, price, '-')
  
  return properties

def get_special_price(index, date_list, reg_price, calendar_reader):
  total_price = 0
  date_list_count = len(date_list)
  for calendar in calendar_reader:
    (special_index, special_date, avail, special_price) = calendar
    if index == special_index and get_datetime(special_date) in date_list and avail == '1':
      total_price += int(special_price)
      date_list_count -= 1
  
  # regular price for the other nights
  for i in range(date_list_count):
    total_price += int(reg_price)
        
  return total_price

     
def get_date_range(date_start, date_end):
    one_day = datetime.timedelta(days=1)
    date_diff = (get_datetime(date_end) - get_datetime(date_start)).days
     
    date_list = []
    i = 0
    curr_date = get_datetime(date_start)
    
    #populate date array
    while i < date_diff:
      date_list.append(curr_date)
      curr_date = curr_date + one_day
      i += 1
   
    return (date_diff, date_list)


def get_datetime(date):
  date_arr = date.split('-')
  
  if date_arr:
    return datetime.date(int(date_arr[0]), int(date_arr[1].strip('0')), int(date_arr[2]))

if __name__ == '__main__':
  main()
