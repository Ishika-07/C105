import csv
import math

with open ("data.csv", newline='') as f:
    reader = csv.reader(f)
    fileData= list(reader)

sum = 0
n = len(fileData)

for number in fileData:
    sum = sum + float(number[0])
mean = sum/n
print("Mean is " + str(sum/n))
squareList =[]

for number in fileData:
    a = int(number[1]) - mean
    a = a**2
    squareList.append(a)

sum_v = 0
for variants in squareList:
    sum_v = sum_v + variants

result =sum_v/n
std = math.sqrt(result)
print(std)