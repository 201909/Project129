import csv
data1 = []
data2 = []

with open ("C:/Users/islam/Byju-coding/class/Class129/final.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data1.append(i)
with open ("C:/Users/islam/Byju-coding/class/Class129/PRO-129-Datasets-main/archive_dataset.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data2.append(i)
headers1 = data1[0]
planet_data1 = data1[1:]
headers2 = data2[0]
planet_data2 = data2[1:]
headers = headers1 + headers2
planet_data = []

for index, i in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+[planet_data2[index]])
with open("merge_dataset.csv", "+a") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)