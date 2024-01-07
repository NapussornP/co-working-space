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
date = StringVar()
date1 = StringVar()

#name
lb = Label(mywin, text = 'Username',font=('Tahoma',11))
lb.grid(row=1,column=0,padx=4,pady=9)

inp = Entry(mywin,textvariable=name)
inp.grid(row=1,column=1,pady=9)
inp.focus()

#Date
d = Label(mywin, text = 'Date',font=('Tahoma',11))
d.grid(row=2,column=0,padx=4,pady=6)

d = Entry(mywin,textvariable = date)
d.grid(row=2,column=1,pady=6)


#time
st = Label(mywin, text = 'Start time',font=('Tahoma',11))
st.grid(row=3,column=0,padx=4,pady=8)

inp_st = Entry(mywin, textvariable=start_time)
inp_st.grid(row=3,column=1,pady=8)

et =  Label(mywin, text='End time',font=('Tahoma',11))
et.grid(row=3,column=2,padx=4,pady=10)

inp_et = Entry(mywin,textvariable=end_time)
inp_et.grid(row=3,column=3,padx=4,pady=10)



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

#calculate button per people
btCAL = Button(mywin,text='calculate',width=10,command=calprice)
btCAL.grid(row=4,column=2)

R1 = Label(mywin, textvariable=result,font=('Tahoma',14),fg='red')
R1.grid(row=4,column=1,pady=7)

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
    
    btday = Button(myowner,text='Calculate',width=10) #ยังไม่ใส่command
    btday.grid(row=2,column=2,padx=4,pady=6)

    per_month = Label(myowner,text='Earned income/month',font=('Tahoma',11))
    per_month.grid(row=3,column=0,padx=4,pady=6)

    btmonth = Button(myowner,text='Calculate',width=10) #command
    btmonth.grid(row=3,column=2,padx=4,pady=6)

    myowner.mainloop()

#button for owner
btnext = Button(mywin,text='for owner',width=10,command=for_owner)
btnext.grid(row=5,column=3)
