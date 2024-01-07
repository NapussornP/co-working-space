from tkinter import*
import csv

mywin=Tk()
mywin.title('Calculate service fees for Co-working space')
mywin.minsize(400,360)

head=Label(mywin,text='Co-working space',font=('Tahoma',20,'bold'))
head.grid(row=0,columnspan=6,pady=7)

#variable
start_time = StringVar()
end_time = StringVar()
result = StringVar()
name = StringVar()
date = StringVar() #####
date1 = StringVar()
month = StringVar() ########

lst_def=[]

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
    try:
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
        #return total_price
        result.set('{} Hr , {} THB'.format(hr,total_price))
        
        ddmmyy = date.get()
        customer_name = name.get()
        #inputstart = str(inp_st.get())
        #inputend = str(inp_et.get())
        #ttprice = calprice(inputstart,inputend)
        lst_def.append(str(ddmmyy))
        lst_def.append(str(start))
        lst_def.append(str(end))
        lst_def.append(str(customer_name))
        lst_def.append(str(hr))
        lst_def.append(str(total_price)) #####
        
        filepath = 'coworkingspace.csv'
        #detail = ['Date','Start time','End time','Name','Total hour','Total price']
        with open (filepath,'a',encoding='utf-8') as outfile:
            writer = csv.writer(outfile,lineterminator='\n')
            #writer.writerow(detail)
            writer.writerow(lst_def)
        lst_def.clear()
    except Exception as e:
        print(e)

#name
lb = Label(mywin, text = 'Username',font=('Tahoma',11))
lb.grid(row=1,column=0,padx=4,pady=9)

inp = Entry(mywin,textvariable=name)
inp.grid(row=1,column=1,pady=9)
inp.focus()

#Date
in_d = Label(mywin, text = 'Date',font=('Tahoma',11))
in_d.grid(row=2,column=0,padx=4,pady=6)

in_d = Entry(mywin,textvariable = date)
in_d.grid(row=2,column=1,pady=6)


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
##################

#cal per day
def calday():
    try:
        #lst_perday = ['Total per day']
        filepath = 'coworkingspace.csv'
        with open(filepath,'r',encoding ='utf-8') as infile:
            read = csv.reader(infile)
            mylist = list(read)
        sum_day = 0
        for loop in mylist:
            sum_day += eval(loop[5])

        '''lst_perday.append(sum_day)
        filepath = 'coworkingspace.csv'
        with open (filepath,'a',encoding='utf-8') as outfile:
            writer = csv.writer(outfile,lineterminator='\n')
            writer.writerow(lst_perday)
        '''
    except Exception as e:
        print(e)

    while True:
        ddmmyy = date.get()
        mm = ((str(ddmmyy))['''ใส่ ... : ... ''' ])
        if mm == 1:
            mm1 = sum_day
        elif mm == 2:
            mm2 = sum_day
        elif mm == 3:
            mm3 = sum_day
        elif mm == 4:
            mm4 = sum_day
        elif mm == 5:
            mm5 = sum_day
        elif mm == 6:
            mm6 = sum_day
        elif mm == 7:
            mm7 = sum_day
        elif mm == 8:
            mm8 = sum_day
        elif mm == 9:
            mm9 = sum_day
        elif mm == 10:
            mm10 = sum_day
        elif mm == 11:
            mm11 = sum_day
        elif mm == 12:
            mm12 = sum_day
        result.set('{} THB'.format(mm))
        
#cal per month
def calmonth():
    while True:
        ipmonth = month.get()
        permm = int(ipmonth)
        if permm == 1:
            permm1 = mm1
        elif permm == 2:
            permm2 = mm2
        elif permm == 3:
            permm3 = mm3
        elif permm == 4:
            permm4 = mm4
        elif permm == 5:
            permm5 = mm5
        elif permm == 6:
            permm6 = mm6
        elif permm == 7:
            permm7 = mm7
        elif permm == 8:
            permm8 = mm8
        elif permm == 9:
            permm9 = mm9
        elif permm == 10:
            permm10 = mm10
        elif permm == 11:
            permm11 = mm11
        elif permm == 12:
            permm12 = mm12
        result.set('{} THB'.format(permm))
    '''try:
        #lst_permonth = ['Total per month']
        filepath = 'coworkingspace.csv'
        with open(filepath,'r',encoding ='utf-8') as infile:
            read = csv.reader(infile)
            mylist = list(read)
        #sum_month=0
        #for loop in mylist:
            #sum_month += eval(loop[....])

        #lst_permonth.append(sum_month)'''
    
'''owner page'''

def for_owner():
    myowner=Tk()
    myowner.title('for owner')
    myowner.minsize(400,360)

    head1=Label(myowner,text='Earned income',font=('Tahoma',20,'bold'))
    head1.grid(row=0,columnspan=6,pady=7)

    lb1 = Label(myowner, text = 'Date',font=('Tahoma',11))
    lb1.grid(row=1,column=0,padx=4,pady=9)

    inp1 = Entry(myowner,textvariable = date)
    inp1.grid(row=1,column=1,pady=9)

    per_day = Label(myowner,text='Earned income/day',font=('Tahoma',11))
    per_day.grid(row=2,column=0,padx=4,pady=6)
    
    btday = Button(myowner,text='Calculate',width=10,command=calday) 
    btday.grid(row=2,column=2,padx=4,pady=6)

    lb2 = Label(myowner, text = 'Month',font=('Tahoma',11))
    lb2.grid(row=3,column=0,padx=4,pady=9)

    inp2 = Entry(myowner,textvariable = month)
    inp2.grid(row=3,column=1,pady=9)
    
    '''def selected():
        mylb = Label(myowner,text=clicked.get()).pack()
        if clicked.get() == '01':
            
    #months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    #clicked = StringVar()
    #clicked.set(months[0])
    #drop = OptionMenu(myowner,clicked,*months)
    #drop.grid(row=3,column=2,padx=4,pady=6)'''
    
    per_month = Label(myowner,text='Earned income/month',font=('Tahoma',11))
    per_month.grid(row=4,column=0,padx=4,pady=6)

    btmonth = Button(myowner,text='Calculate',width=10,command=calday)
    btmonth.grid(row=4,column=2,padx=4,pady=6)

    myowner.mainloop()


#button for owner
btnext = Button(mywin,text='for owner',width=10,command=for_owner)
btnext.grid(row=4,column=3)



mywin.mainloop()
