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
i = 0
for target in targets:                                                                              # target from "C0A880" to "C0F9A0"
    target_data = list(filter(lambda item: item['station_id'] == target, data))
    num = 0
    pres_total = 0
    for i in range(len(target_data)):                                                               # i from 0 to [number of data of target - 1]
        if float(target_data[i].get("PRES")) != -99 and float(target_data[i].get("PRES")) != -999:  # discard the value = -99 or -999
            pres_total += float(target_data[i].get("PRES"))
            num += 1
    if num != 0:
        pres_mean = pres_total / num
        result.append([target,round(pres_mean, 1)])
    else:
        result.append([target,"None"])
#=======================================

# Part. 4
#=======================================
# Print result
print(result)
#========================================