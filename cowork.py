from tkinter import *
mywin=Tk()
mywin.title('คำนวณค่าบริการร้าน Co-working space')
mywin.minsize(400,400)

#name
name=StringVar()
lb = Label(mywin, text = 'ชื่อผู้เข้าใช้บริการ')
lb.grid(row=0,column=0)

inp = Entry(mywin,textvariable=name)
inp.grid(row=0,column=1)
inp.focus()


#day
day=StringVar()
lb1 = Label(mywin, text = 'ว/ด/ป')
lb1.grid(row=0,column=2,sticky=E)

inp1 = Entry(mywin,textvariable = day)
inp1.grid(row=0,column=3,sticky=E)

#time
intime=StringVar()
lb2 = Label(mywin, text = 'เวลาเข้า')
lb2.grid(row=1,column=0)

inp2 = Entry(mywin, textvariable=intime)
inp2.grid(row=1,column=1)

outtime=StringVar()
lb3 =  Label(mywin, text='เวลาออก')
lb3.grid(row=1,column=2)

inp3 = Entry(mywin,textvariable=outtime)
inp3.grid(row=1,column=3)