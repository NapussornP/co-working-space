import csv
filepath = 'working.csv'
with open(filepath,'r',encoding='utf-8')as infile:
    rd = csv.reader(infile)
    mylist = list(rd)
    
sum_day=0    
for col in mylist:
    sum_day += eval(col[6])
    

print('{}'.format(sum_day))