from csv import  reader

with open('..\TestData\login.txt') as file:
    csv_Reader = list(reader(file))[::-1]
    print(csv_Reader[1][0])