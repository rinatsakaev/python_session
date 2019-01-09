import csv
if __name__ == '__main__':
    with open("file.csv") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            print(row)
