from tkinter import*
from tkinter.ttk import Combobox
from tkinter.messagebox import*
import datetime
from playsound import playsound

root=Tk()
 

def alarm():
    if x.get()=="AM":
        h=int(c.get())
        m=int(c1.get())

    if x.get()=="PM":
        h=int(c.get())+12
        m=int(c1.get())
    
    showinfo("alarm notication","alarm has been set")
    while True:
        if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
                playsound('https://musikringtone.com//downloads//5380//')
                showinfo("alarm notificarion","wake upke")
                break
root.title(" My Alaram Clock")
root.geometry("450x300")


l1=Label(root,text="Hour")
l1.grid(row=0,column=0)
hour=list(range(0,13))
c=Combobox(root,values=hour)
c.grid(row=0,column=1)

l2=Label(root,text="Minute")
l2.grid(row=1,column=0)
minute=list(range(0,61))
c1=Combobox(root,values=minute)
c1.grid(row=1,column=1 )

x=Combobox(root,value=["AM","PM"])
x.grid(row=3,column=1)
l3=Label(root,text="AM OR PM")
l3.grid(row=3,column=0)

btn=Button(root,bg="red",fg="black",text="set alarm",command=alarm)
btn.grid(row=8,column=1)

clockImage=PhotoImage(file="/home/bulbul/Downloads/index.png")
img=Label(root,image=clockImage)
img.grid(row=4,column=0)

root.mainloop()


