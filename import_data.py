import csv
import random


with open("test_ver2.csv","r",encoding="utf-8") as csvfile:     #13647310
         reader = csv.DictReader(csvfile)
         column = [row['ncodpers'] for row in reader]

#column=[1, 2, 3 ,4 ,5 ];
N=len(column)

with open("train_ver2.csv", "r", encoding="utf-8") as csvfile:  # 13647310
    reader = csv.reader(csvfile)
    for i, rows in enumerate(reader):
           if i == 0:
            row = rows
#print(row)

product=row[24:len(row)];
#product=['a','b','c','d','e','f','g','h'];
data=[];
user=[];
L=[n for n in range(0,len(product))];
L.remove(2);
for i in range(0,len(column)):
    user.append(column[i]);
    user.append(product[2]);
    resultList = random.sample(L,6);   #1到24中不重复产生7个数
    d = [product[j] for j in resultList];
    for t in d:
        user.append(t);
    data.append(user);
    user=[];
 #   print(data)

csvfile = open('result.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow(['ncodpers','added_products'])
writer.writerows(data)
csvfile.close()


