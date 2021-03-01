# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061113.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
# target_data = data[:10]
targets = ["C0A880", "C0F9A0", "C0G640", "C0R190", "C0X260"]
result = []
for target in targets:
   target_data = list(filter(lambda item: item['station_id'] == target, data))
   pres_column = [column['PRES'] for column in target_data]

   num = 0
   pres_total = 0
   for pres_value in pres_column:
      if float(pres_value) != -99 and float(pres_value) != -999:
         num += 1
         pres_total += float(pres_value)
         pres_mean = pres_total / num
      #print(num)
   if num != 0:
      result.append([target,round(pres_mean, 1)])
   else:
      result.append([target,"None"])

print(result)
#=======================================

# Part. 4
#=======================================
# Print result
# print(target_data)
#========================================