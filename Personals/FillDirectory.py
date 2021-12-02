from csv import writer
dictionary = [i for i in range(201)]

with open("C:\\JetBrains_Projects\\pycharm_projects\\Übungen\\Personals\\TestCSV.csv", "w") as f:
    flwriter = writer(f)
    for i in dictionary[10::10]:
        flwriter.writerow(dictionary[i-10:i])

print(dictionary[10::10])