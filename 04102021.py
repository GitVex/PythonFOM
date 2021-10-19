import re
import csv

# =-=-=-=-=-=-=- Nr. 1a =-=-=-=-=-=-=-
with open("/NASA_access_log_Jul95", "r") as f:
	log = f.readlines()

# b
# for i in log[:10]:
# print(i)

# =-=-=-=-=-=-=- Nr. 2 =-=-=-=-=-=-=-
logfile = log[:10]

AccessSearch = re.compile(r'(^(?:.+?(?= )))+.+(\[.*\])+.+(\".*\")*')
AccessAccessorList = []
AccessDateList = []
AccessInfoList = []

for entry in logfile:
	matchObject = AccessSearch.search(entry)
	if matchObject:
		AccessAccessorList.append(matchObject.groups("1"))
		AccessDateList.append(matchObject.groups("2"))
		AccessInfoList.append(matchObject.groups("3"))
	else:
		print("No match found in:\t", entry)

complete = []

print(len(logfile), len(AccessAccessorList), len(AccessDateList), len(AccessInfoList))

for i in range(0, len(AccessDateList)):
	complete.append((AccessAccessorList[i], AccessDateList[i], AccessInfoList[i]))

# =-=-=-=-=-=-=- Nr. 3 =-=-=-=-=-=-=-

# n = 0
# for i in complete:
# n += 1
# print(n, i)

# =-=-=-=-=-=-=- Nr. 5 =-=-=-=-=-=-=-

with open("/04102021/04102021CSVOutput.csv", "w") as f:
	f_writer = csv.writer(f, delimiter="@", quotechar="'", quoting=csv.QUOTE_MINIMAL)
	for i in range(0, len(complete)):
		f_writer.writerow(complete[i])
