from os import read
from tkinter import*
from tkinter import ttk
import csv
from datetime import datetime
import pandas
from pandas.core.frame import DataFrame
from tkcalendar import DateEntry 
import pandas as pd

mywin=Tk()
mywin.title('Calculate service fees for Co-working space')
mywin.minsize(400,360)

head=Label(mywin,text='Co-working space',font=('Tahoma',20,'bold'))
head.grid(row=0,columnspan=6,pady=7)

#--------------------------------------variable----------------------------------------------
start_time = StringVar()
end_time = StringVar()
result = StringVar()
name = StringVar()
date = StringVar()
date1 = StringVar()
result_day = StringVar()
month = StringVar()

lst_def=[]
lst_add=[]

#------------------------------------price/people-------------------------------------------
def calprice(): #ใส่พารา
    while True:
        start = start_time.get()
        end = end_time.get()
        st_hr = int(start[0:2])
        st_min = int(start[3:5])
        e_hr = int(end[0:2])
        e_min = int(end[3:5])

        
        if 7<=st_hr<=24 and 7<=e_hr<=24 and 0<=st_min<=60 and 0<=e_min<=60:
            total_min = (e_hr*60 + e_min) - (st_hr*60 + st_min)
            break
        else:
            print('please enter Start time and End time again ')
   

    if total_min%60==0:
        hr = total_min//60
    else:
        hr = total_min//60 + 1

    if hr >= 1:
        total_price = hr*60
    elif hr >= 2:
        total_price = hr*40
    elif hr <= 3:
        total_price = hr*30
    result.set('{} Hr , {} THB'.format(hr,total_price))

    dd = date.get()
    mm = month.get()
    customer_name = name.get()
    lst_def.append(str(dd))
    lst_def.append(str(mm))
    lst_def.append(str(start))
    lst_def.append(str(end))
    lst_def.append(str(customer_name))
    lst_def.append(str(hr))
    lst_def.append(str(total_price))

    filepath = 'working.csv'
    with open (filepath,'a',encoding='utf-8') as outfile:
        writer = csv.writer(outfile,lineterminator='\n')
        writer.writerow(lst_def)
    

#--------------------------------------------------gui price----------------------------------------------------------
#name
lb = Label(mywin, text = 'Username',font=('Tahoma',11))
lb.grid(row=1,column=0,padx=4,pady=9)

inp = Entry(mywin,textvariable=name)
inp.grid(row=1,column=1,pady=9)
inp.focus()

#Date
in_d = Label(mywin, text = 'Date',font=('Tahoma',11))
in_d.grid(row=2,column=0,pady=6)

in_d = Entry(mywin,textvariable = date)
in_d.grid(row=2,column=1,pady=6)

m = ttk.Combobox(mywin,width=8,textvariable=month)
m['values'] = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
m.grid(row=2,column=2,pady=6)

#time
st = Label(mywin, text = 'Start time',font=('Tahoma',11))
st.grid(row=3,column=0,padx=4,pady=8)

inp_st = Entry(mywin, textvariable=start_time)
inp_st.grid(row=3,column=1,pady=8)

et =  Label(mywin, text='End time',font=('Tahoma',11))
et.grid(row=3,column=2,padx=4,pady=10)

inp_et = Entry(mywin,textvariable=end_time)
inp_et.grid(row=3,column=3,padx=4,pady=10)

#calculate button per people
btCAL = Button(mywin,text='calculate',width=10,command=calprice)
btCAL.grid(row=4,column=2)

R1 = Label(mywin, textvariable=result,font=('Tahoma',14),fg='red')
R1.grid(row=4,column=1,pady=7)


   
#--------------------------------------------------------------income month------------------------------------------------------------
def income_month():

    filepath = 'working.csv'
    with open(filepath,'r',encoding='utf-8')as infile:
        rd = csv.reader(infile)
        mylist = list(rd)
    
    sum_day=0    
    for col in mylist:
        sum_day += eval(col[6])

    result_day.set('{} THB'.format(sum_day))
    
            
    

#button for owner
btnext = Button(mywin,text='for owner',width=10,command=income_month)
btnext.grid(row=4,column=3)
R_day = Label(mywin, textvariable=result_day,font=('Tahoma',11))
R_day.grid(row=5,column=2,pady=7) 


mywin.mainloop()