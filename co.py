#Gui

from tkinter import *
from tkinter.font import BOLD
mywin=Tk()
mywin.title('Calculate service fees for Co-working space')
mywin.minsize(400,350)

Label(mywin,text='Co-working space').grid(font=('BOLD',20))

#name
name=StringVar()
lb = Label(mywin, text = 'Username')
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

'''#เจ้าของ
lb4= Label(mywin, textvariable=display)
lb4.(row=3,sticky=CENTER,fg=red)'''

#buttomcalculate

'''btCAL = Buttom(mywin, text='คำนวณ' width=15,command=sayhello)
btCAL.grid(row=4,sticky=E)'''

mywin.mainloop()

