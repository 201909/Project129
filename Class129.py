import csv
data = []

with open ("C:/Users/islam/Byju-coding/class/Class129/PRO-129-Datasets-main/archive_dataset.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data.append(i)
headers = data[0]
planet_data = data[1:]

for data_point in planet_data:
    data_point[2]=data_point[2].lower()
planet_data.sort(key = lambda planet_data:planet_data[2])
with open("archive_dataset_sorted.csv", "+a") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)

with open("C:/Users/islam/Byju-coding/class/Class129/PRO-129-Datasets-main/archive_dataset.csv") as input, open("archive_dataset_sorted1.csv", "w", newline="") as output:
    writer = csv.writer(output)
    for i in csv.reader(input):
        if any (field.strip() for field in i):
            writer.writerow(i)