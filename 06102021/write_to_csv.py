import os
import csv
from collections.abc import Iterable


def write_to_csv(filename, content):
	cd = os.getcwd() + '\\' + filename
	with open(cd, "w") as file:
		writer = csv.writer(file, delimiter=",", quotechar="'")
		if isinstance(content, Iterable):
			writer.writerow(content)
		else:
			writer.writerow(content)


print(os.getcwd())
write_to_csv("test2.csv", [x for x in range(0, 100)])
